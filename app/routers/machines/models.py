from sqlalchemy import Column, String, Integer

from app.database.database import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    mac = Column(String)
    name = Column(String, unique=True)
    description = Column(String, default="A HomeAPI Compatible machine")
