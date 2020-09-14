from sqlalchemy import Column, String, Boolean, Integer

from database.database import Base


class Light(Base):
    __tablename__ = "lights"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    name = Column(String, unique=True)
    description = Column(String, default="A YeeLight Bulb")
