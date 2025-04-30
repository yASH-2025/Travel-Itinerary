from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=False)
    nights = Column(Integer, nullable=False)
    days = relationship("Day", back_populates="itinerary")

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'))
    hotel = Column(String)
    transfer = Column(String)
    activities = Column(String)  # Comma-separated
    itinerary = relationship("Itinerary", back_populates="days")
