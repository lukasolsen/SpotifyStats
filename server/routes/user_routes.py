from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from models import UserModel
from database import get_table, add_user
from passlib.hash import bcrypt

router = APIRouter()

# Secret key for JWT token (change this to a strong secret in production)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class UserInDB(UserModel):
    hashed_password: str


class UserInResponse(UserModel):
    access_token: str
    token_type: str


class UserInRequest(BaseModel):
    username: str
    password: str
    email: str


class LoginRequest(BaseModel):
    username: str
    password: str


def get_password_hash(password):
    return bcrypt.hash(password)


def verify_password(plain_password, hashed_password):
    print(plain_password, hashed_password)

    print(bcrypt.verify(plain_password, hashed_password))
    return bcrypt.verify(plain_password, hashed_password)

# Create JWT token


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(username: str):
    # Use your database function here to fetch user data
    print("Username from 'get_user' ->", username)
    user_data = get_table("users")
    print(user_data)
    user = next(
        (item for item in user_data if item[1] == username), None)
    print(user)
    if user:
        user_dict = {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "password": user[3],
            "plan": user[4]
        }
        return user_dict
    return None


def create_user(user: UserInRequest):
    hashed_password = get_password_hash(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "plan": "free"
    }
    # Use your database function here to insert new user
    add_user(new_user)
    return new_user


@router.post("/register")
async def register_user(user: UserInRequest):
    print(user)
    db_user = get_user(username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = create_user(user=user)
    print(new_user)

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login")
async def login_user(user: LoginRequest):
    print("Username ->", user.username)
    db_user = get_user(username=user.username)
    if db_user is None or not verify_password(user.password, db_user["password"]):
        print("Incorrect username or password")
        raise HTTPException(
            status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token")
async def get_token(token: str):
    try:
        # use jwt verify instead
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")
