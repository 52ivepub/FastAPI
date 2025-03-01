from fastapi import APIRouter, Depends, HTTPException, Response, status



UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
 
)


IncorrectEmailOrPassword = HTTPException(
    status = status.HTTP_401_UNAUTHORIZED,
    datail="Неверная почта или пароль",
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
     detail="Токен истек",
)

TokenAbsentExtension = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    datail="Токен отсутствует",
)


IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Некорректный формат токена",
)


UserIdNotPresentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)