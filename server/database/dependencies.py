from passlib.hash import bcrypt
from database.database import get_table, add_user
from models.user import User


def get_password_hash(password):
    return bcrypt.hash(password)


def verify_password(plain_password, hashed_password):
    print(plain_password, hashed_password)

    print(bcrypt.verify(plain_password, hashed_password))
    return bcrypt.verify(plain_password, hashed_password)


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
            "disabled": user[4],
            "plan": user[5]
        }
        return user_dict
    return None


def create_user(user: User):
    hashed_password = get_password_hash(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "disabled": False,
        "plan": "free"
    }
    # Use your database function here to insert new user
    add_user(new_user)
    return new_user
