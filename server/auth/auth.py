from fastapi import Depends, HTTPException, status
from jose import jwt
from datetime import datetime, timedelta
from models.user import UserModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return bcrypt.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)


def create_access_token(user: UserModel, expires_delta: timedelta = None):
    to_encode = user.dict()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
