from pydantic import BaseModel
from typing import List

class DayCreate(BaseModel):
    day_number: int
    hotel: str
    transfer: str
    activities: List[str]

class ItineraryCreate(BaseModel):
    region: str
    nights: int
    days: List[DayCreate]

class DayOut(DayCreate):
    id: int

class ItineraryOut(ItineraryCreate):
    id: int
    days: List[DayOut]
