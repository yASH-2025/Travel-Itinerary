from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.models.itinerary import Itinerary
from app.db.session import get_db
from fastapi import Depends

router = APIRouter()

@router.get("/recommendations/{nights}")
def get_recommendation(nights: int, db: Session = Depends(get_db)):
    rec = db.query(Itinerary).filter(Itinerary.nights == nights).first()
    if not rec:
        return {"message": "No itinerary found for given duration"}
    return rec