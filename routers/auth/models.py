from sqlalchemy import Column, String, Integer, Boolean

from database.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean)
