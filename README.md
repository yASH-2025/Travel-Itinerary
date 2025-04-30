1. Set Up the Environment -> Make sure you have Python 3.8+ installed. Then:
    cd path/to/travel_itinerary
    python -m venv venv
    source venv/bin/activate     # On Windows: venv\Scripts\activate
    pip install -r requirements.txt


2. Run the FastAPI Server -> Start the server using uvicorn:
    uvicorn app.main:app --reload
