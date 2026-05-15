from pydantic import BaseModel
from typing import Optional


class Point(BaseModel):
    id: str
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None