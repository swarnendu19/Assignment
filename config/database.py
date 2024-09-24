from config.settings import settings 
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User  


async def startDB():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(database=client.db_name, document_models=[User])