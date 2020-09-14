from sqlalchemy.orm import Session

from . import models, schemas


def get_light_by_name(db: Session, name: str):
    return db.query(models.Light).filter(models.Light.name == name).first()


def get_lights(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Light).offset(skip).limit(limit).all()


def create_light(db: Session, light: schemas.LightCreate):
    db_light = models.Light(**light.dict())
    db.add(db_light)
    db.commit()
    db.refresh(db_light)
    return db_light


def delete_light_by_name(db: Session, name: str):
    db_light = db.query(models.Light).filter(models.Light.name == name).first()
    db.delete(db_light)
    db.commit()
    return db_light
