from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import user_routes
from routes import data_routes

app = FastAPI()

# cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# For all routes make them start with /api/v1

app.include_router(user_routes.router, prefix="/api/v1")
app.include_router(data_routes.router, prefix="/api/v1")
