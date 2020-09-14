from typing import Optional

from pydantic import BaseModel

# TODO: use fastapi's Query() to validate ip & mac format


class LightBase(BaseModel):
    ip: str
    name: str
    description: Optional[str] = None


class LightCreate(LightBase):
    pass


class Light(LightBase):
    id: int

    class Config:
        orm_mode = True
