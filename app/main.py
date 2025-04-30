from fastapi import FastAPI
from app.routes import itinerary
from app.mcp import recommender
from app.db.session import Base, engine
from app.db.seed_data import seed

app = FastAPI()
Base.metadata.create_all(bind=engine)
seed()

app.include_router(itinerary.router)
app.include_router(recommender.router)