from sqlalchemy import select
from app.datebase import async_session_maker
from app.bookings.models import Bookings


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model )
            bookings = await session.execute(query)
            return bookings.scalars().all()
