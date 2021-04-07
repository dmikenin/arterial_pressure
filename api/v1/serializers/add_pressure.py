from pydantic import BaseModel
from typing import Optional

class AddPressureSerializer(BaseModel):
    upper: int
    down: int
    heartbeat: Optional[int] = 0
    timezone: Optional[int] = 0