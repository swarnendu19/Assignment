from fastapi import FastAPI
from config.database import startDB
from contextlib import asynccontextmanager
from routers import auth
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    await startDB()
    print("MongoDB Connected successfully..")
    
    # Yield to allow the application to run
    yield

app = FastAPI(lifespan=lifespan)   

origins = [
    settings.CLIENT_ORIGIN,  # Ensure this is correctly set
    "http://localhost:3000",  # Example frontend origin
    "http://localhost:8000"   # The backend itself if needed
    "http://localhost:5173"   # The backend itself if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Auth"], prefix='/api/auth')

@app.get("/api/test")
async def root():
    return {"message": "FastAPI is working"}
