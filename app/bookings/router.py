from fastapi import APIRouter
from sqlalchemy import select
from app.bookings.models import Bookings
from app.datebase import async_session_maker
from app.bookings.models import Bookings


router = APIRouter(
    prefix = "/bookings",
    tags = ["Бронирования"],

)

@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings) 
        result = await session.execute(query)
        
        return result.scalars().all()
            

        

    


