from typing import Optional

from pydantic import BaseModel

# TODO: use fastapi's Query() to validate ip & mac format


class MachineBase(BaseModel):
    ip: str
    mac: str
    name: str
    description: Optional[str] = None


class MachineCreate(MachineBase):
    pass


class Machine(MachineBase):
    id: int

    class Config:
        orm_mode = True

