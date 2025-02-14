from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel 

app = FastAPI()

class SHotel(BaseModel):
    adress: str
    name: str
    stars: int





@app.get("/hotels")
def foo(location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool]=None,
        stars: Optional[int]=Query(None, ge=1, le=5)) -> list[SHotel]:


    hotels = [
        {
            "adress": 'ул. Гагарина, 1, Алтай',
            "name": 'Super Hotel',
            "stars": 5,
        },
    ]
    return hotels
 

class SBoking(BaseModel):
    room_id : int
    date_from: date
    date_to: date

@app.post('/bookings')
def add_boking(SBoking):
    pass



