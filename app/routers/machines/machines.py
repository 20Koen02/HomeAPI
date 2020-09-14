from typing import List
from copy import deepcopy
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from app.database.database import SessionLocal, get_db
from app.helper import wol, ping

router = APIRouter()


@router.get("/", response_model=List[schemas.Machine])
async def read_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machines = crud.get_machines(db, skip=skip, limit=limit)
    return machines


@router.post("/", response_model=schemas.Machine)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    db_machine = crud.get_machine_by_name(db, name=machine.name)
    if db_machine:
        raise HTTPException(status_code=400, detail="Machine already registered")
    return crud.create_machine(db=db, machine=machine)


@router.delete("/", response_model=schemas.Machine)
def delete_machine(machine: str, db: Session = Depends(get_db)):
    db_machine = crud.get_machine_by_name(db, name=machine)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return crud.delete_machine_by_name(db, name=machine)


@router.get("/{name}")
async def read_machine(name: str, db: Session = Depends(get_db)):
    db_machine = crud.get_machine_by_name(db, name=name)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    res = vars(db_machine)
    res["is_online"] = ping.ping(db_machine.ip)
    return res


@router.put("/{name}/on", response_model=schemas.Machine)
async def wake_machine(name: str, db: Session = Depends(get_db)):
    db_machine = crud.get_machine_by_name(db, name=name)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")

    wol.wake_up(db_machine.ip, db_machine.mac)
    return db_machine
