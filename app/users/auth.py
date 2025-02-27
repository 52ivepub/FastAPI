import os
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.config import Settings as settings
from pydantic import EmailStr
import dotenv
from app.config import Settings
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

dotenv.load_dotenv()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.getenv("SECRET_KEY"), os.getenv("ALGORITM")
    )
    return encoded_jwt 


async def autenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password ):
        return None
    return user
