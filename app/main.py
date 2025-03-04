from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel 
from app.users.router import router as router_users
from app.bookings.router import router as router_bookings



app = FastAPI()

app.include_router(router_bookings)
app.include_router(router_users)

class HotelsSearchArghs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool]=None,
        stars: Optional[int]=Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

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
 






