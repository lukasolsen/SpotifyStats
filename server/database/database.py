import sqlite3
import os
from models.data import DataModel

# Specify the relative path to the database file
DATABASE_FILE = "your_database.db"

# Create database file if it doesn't exist


def create_database_if_not_exists():
    if not os.path.exists(DATABASE_FILE):
        conn = sqlite3.connect(DATABASE_FILE)
        conn.close()


create_database_if_not_exists()


def create_tables():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create user and track tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            username TEXT,
            email TEXT,
            password TEXT,
            disabled BOOLEAN,
            plan TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            user_id INTEGER,
            timestamp TEXT,
            total_seconds_played REAL,
            offline_seconds REAL,
            online_seconds REAL,
            total_tracks INTEGER,
            total_albums INTEGER,
            total_artists INTEGER,
            tracks TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_table(table: str):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()

    conn.commit()
    conn.close()

    return data


def add_user(user_data: dict):
    required_keys = ['username', 'email', 'password', "disabled", "plan"]
    print(user_data)

    if not all(key in user_data for key in required_keys):
        raise ValueError(
            "User data dictionary should contain all required keys.")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password, disabled, plan) VALUES (:username, :email, :password, :disabled, :plan)",
        user_data
    )

    conn.commit()
    conn.close()


def add_data(data: DataModel):
    required_keys = ['user_id', 'timestamp', 'total_seconds_played', 'offline_seconds', 'online_seconds',
                     'total_tracks', 'total_albums', 'total_artists', 'tracks']

    data_dict = data.dict()
    # Turn the tracks into a string
    data_dict["tracks"] = str(data_dict["tracks"])

    for key in required_keys:
        if key not in data_dict:
            raise ValueError(
                f"Data dictionary should contain all required keys. Missing key: {key}")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO data (user_id, timestamp, total_seconds_played, offline_seconds, online_seconds, total_tracks, total_albums, total_artists, tracks)
        VALUES (:user_id, :timestamp, :total_seconds_played, :offline_seconds, :online_seconds, :total_tracks, :total_albums, :total_artists, :tracks)
        """,
        data_dict  # Pass the data dictionary here
    )

    conn.commit()
    conn.close()


def update_table(table: str, data):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(f"UPDATE {table} SET {data}")

    conn.commit()
    conn.close()


# Define functions for database interactions
try:
    if (get_table("users") == None or get_table("data") == None):
        create_tables()
except:
    create_tables()
