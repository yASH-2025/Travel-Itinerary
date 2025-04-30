from app.db.session import SessionLocal
from app.models.itinerary import Itinerary, Day

def seed():
    db = SessionLocal()
    db.query(Day).delete()
    db.query(Itinerary).delete()

    itinerary = Itinerary(region="Phuket", nights=3)
    db.add(itinerary)
    db.commit()
    db.refresh(itinerary)

    days = [
        Day(day_number=1, hotel="Beach Resort", transfer="Airport Pickup", activities="Relax,Explore", itinerary_id=itinerary.id),
        Day(day_number=2, hotel="Beach Resort", transfer="None", activities="Island Tour,Snorkeling", itinerary_id=itinerary.id),
        Day(day_number=3, hotel="Beach Resort", transfer="Airport Drop", activities="Shopping", itinerary_id=itinerary.id)
    ]

    db.add_all(days)
    db.commit()
    db.close()