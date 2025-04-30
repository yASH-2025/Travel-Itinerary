from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.itinerary import ItineraryCreate, ItineraryOut, DayOut
from app.models.itinerary import Itinerary, Day
from app.db.session import get_db

router = APIRouter()

def serialize_itinerary(itinerary: Itinerary) -> ItineraryOut:
    return ItineraryOut(
        id=itinerary.id,
        region=itinerary.region,
        nights=itinerary.nights,
        days=[
            DayOut(
                id=day.id,
                day_number=day.day_number,
                hotel=day.hotel,
                transfer=day.transfer,
                activities=day.activities.split(",")
            ) for day in itinerary.days
        ]
    )

@router.post("/itineraries/", response_model=ItineraryOut)
def create_itinerary(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    db_itinerary = Itinerary(region=itinerary.region, nights=itinerary.nights)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    for day in itinerary.days:
        db_day = Day(
            day_number=day.day_number,
            hotel=day.hotel,
            transfer=day.transfer,
            activities=",".join(day.activities),
            itinerary_id=db_itinerary.id
        )
        db.add(db_day)
    db.commit()
    db.refresh(db_itinerary)
    return serialize_itinerary(db_itinerary)

@router.get("/itineraries/", response_model=list[ItineraryOut])
def get_itineraries(db: Session = Depends(get_db)):
    itineraries = db.query(Itinerary).all()
    return [serialize_itinerary(itin) for itin in itineraries]