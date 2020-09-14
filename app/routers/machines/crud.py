from sqlalchemy.orm import Session

from . import models, schemas


def get_machine_by_name(db: Session, name: str):
    return db.query(models.Machine).filter(models.Machine.name == name).first()


def get_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Machine).offset(skip).limit(limit).all()


def create_machine(db: Session, machine: schemas.MachineCreate):
    db_machine = models.Machine(**machine.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine


def delete_machine_by_name(db: Session, name: str):
    db_machine = db.query(models.Machine).filter(models.Machine.name == name).first()
    db.delete(db_machine)
    db.commit()
    return db_machine
