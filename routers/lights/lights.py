from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from yeelight import Bulb, BulbException

from database.database import SessionLocal, get_db
from . import schemas, crud

router = APIRouter()
bulbs = {}

bulb_db = SessionLocal()
bulb_lights = crud.get_lights(bulb_db)
for bulb_light in bulb_lights:
    bulbs[bulb_light.name] = Bulb(bulb_light.ip)
bulb_db.close()


def change_light(db, name: str, func: str, arguments=None):
    db_light = crud.get_light_by_name(db, name=name)
    if db_light is None:
        raise HTTPException(status_code=404, detail="Light not found")
    res = vars(db_light)
    try:
        if arguments:
            getattr(bulbs[db_light.name], func)(*arguments)
        else:
            getattr(bulbs[db_light.name], func)()
        props = bulbs[db_light.name].get_properties()
        res["properties"] = props
    except BulbException:
        raise HTTPException(status_code=404, detail="Could not connect to light")
    except AssertionError:
        raise HTTPException(status_code=400, detail="Commands have no effect when the bulb is off")

    return res


@router.get("/", response_model=List[schemas.Light])
async def read_lights(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lights = crud.get_lights(db, skip=skip, limit=limit)
    return lights


@router.post("/", response_model=schemas.Light)
def create_light(light: schemas.LightCreate, db: Session = Depends(get_db)):
    db_light = crud.get_light_by_name(db, name=light.name)
    if db_light:
        raise HTTPException(status_code=400, detail="Light already registered")
    new_light = crud.create_light(db=db, light=light)
    bulbs[new_light.name] = Bulb(new_light.ip)
    return new_light


@router.delete("/", response_model=schemas.Light)
def delete_light(light: str, db: Session = Depends(get_db)):
    db_light = crud.get_light_by_name(db, name=light)
    if db_light is None:
        raise HTTPException(status_code=404, detail="Light not found")
    deleted_light = crud.delete_light_by_name(db, name=light)
    del bulbs[deleted_light.name]
    return deleted_light


@router.get("/{name}")
async def read_light(name: str, db: Session = Depends(get_db)):
    db_light = crud.get_light_by_name(db, name=name)
    if db_light is None:
        raise HTTPException(status_code=404, detail="Light not found")
    res = vars(db_light)
    try:
        props = bulbs[db_light.name].get_properties()
        res["properties"] = props
    except BulbException:
        res["properties"] = {}
    return res


@router.put("/{name}/on")
async def turn_light_on(name: str, db: Session = Depends(get_db)):
    return change_light(db, name, "turn_on")


@router.put("/{name}/off")
async def turn_light_off(name: str, db: Session = Depends(get_db)):
    return change_light(db, name, "turn_off")


@router.put("/{name}/toggle")
async def toggle_light(name: str, db: Session = Depends(get_db)):
    return change_light(db, name, "toggle")


@router.put("/{name}/brightness")
async def set_light_brightness(name: str,
                               value: int = Query(..., ge=1, le=100),
                               db: Session = Depends(get_db)):
    return change_light(db, name, "set_brightness", [value])


@router.put("/{name}/rgb")
async def set_rgb_value(name: str,
                        red: int = Query(..., ge=0, le=255),
                        green: int = Query(..., ge=0, le=255),
                        blue: int = Query(..., ge=0, le=255),
                        db: Session = Depends(get_db)):
    return change_light(db, name, "set_rgb", [red, green, blue])


@router.put("/{name}/hsv")
async def set_hsv_value(name: str,
                        hue: int = Query(..., ge=0, le=359),
                        saturation: int = Query(..., ge=0, le=100),
                        brightness: Optional[int] = Query(None, ge=0, le=100),
                        db: Session = Depends(get_db)):
    return change_light(db, name, "set_hsv", [hue, saturation, brightness])


@router.put("/{name}/temperature")
async def set_temperature_value(name: str,
                                temperature: int = Query(..., ge=1700, le=6500),
                                db: Session = Depends(get_db)):
    return change_light(db, name, "set_color_temp", [temperature])
