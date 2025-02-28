from fastapi import APIRouter, Request
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix = "/bookings",
    tags = ["Бронирования"],

)   

@router.get("")
async def get_bookings(request: Request):
    return await BookingDAO.find_all()


    # return await BookingDAO.find_all()
     
            

        

    



