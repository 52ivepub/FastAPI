from fastapi import FastAPI

app = FastAPI()

@app.get("/hotel/{hotel_id}")
def foo(hotel_id:int, date_from, date_to):
    
    return hotel_id, date_from, date_to

# import requests

# r = requests.get(
#     "http://127.0.0.1:8000/hotel/12",
#     params  = {"date_from": "today", 'date_to':"' }
# )
