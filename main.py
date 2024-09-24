from fastapi import FastAPI
from config.database import startDB
from contextlib import asynccontextmanager
from routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    await startDB()
    print("MongoDB Connected successfully..")
    
    # Yield to allow the application to run
    yield

app = FastAPI(lifespan=lifespan)  # Set the lifespan function here

app.include_router(auth.router, tags=["Auth"], prefix='/api/auth')

@app.get("/api/test")
async def root():
    return {"message": "FastAPI is working"}
