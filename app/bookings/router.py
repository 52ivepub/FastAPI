from fastapi import APIRouter
from app.bookings.dao import BookingDAO

router = APIRouter(
    prefix = "/bookings",
    tags = ["Бронирования"],

)   

@router.get("")
async def get_bookings():
    result = BookingDAO.find_one_or_none(id=1)
    return await result
            

        

    



