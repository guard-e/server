from typing import List, Optional
from pydantic import BaseModel

class ContrBase(BaseModel):
    sn: int
    model: int
    address: int
    fw_version: int
    ctrl_flags: int
    bank_size: int
    pass_point: int


class ContrCreate(ContrBase):
    pass


class Contr(ContrBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ConvBase(BaseModel):
    port_type: int
    port_name: str
    model: int
    sn: int


class ConvCreate(ConvBase):
    pass


class Conv(ConvBase):
    id: int
    items: List[Contr] = []

    class Config:
        orm_mode = True