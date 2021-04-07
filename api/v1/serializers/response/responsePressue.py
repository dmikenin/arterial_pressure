from typing import List, Dict

from pydantic import BaseModel


class ResponseAddPressue(BaseModel):
    status: str
    message: str


class ResponsePressue(BaseModel):
    id: str
    upper: int
    down: int
    heartbeat: int
    date: str
    time: str


class ResponseGetListPressue(ResponseAddPressue):
    pressure: List[
        ResponsePressue
    ]


class ResponseGetOnePressue(ResponseAddPressue):
    pressure: ResponsePressue
