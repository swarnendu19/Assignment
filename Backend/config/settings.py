from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mongodb+srv://swarnendumaity2003:Swarna2003@cluster0.la02l0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE", "default_db_name")  
    JWT_PUBLIC_KEY: str = os.getenv("JWT_PUBLIC_KEY", "default_public_key")  
    JWT_PRIVATE_KEY: str = os.getenv("JWT_PRIVATE_KEY", "default_private_key")  
    REFRESH_TOKEN_EXPIRES_IN: int = int(os.getenv("REFRESH_TOKEN_EXPIRES_IN", 3600))   
    ACCESS_TOKEN_EXPIRES_IN: int = int(os.getenv("ACCESS_TOKEN_EXPIRES_IN", 3600))   
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")   
    CLIENT_ORIGIN: str = os.getenv("CLIENT_ORIGIN", "http://localhost:8000")   

 
settings = Settings()
