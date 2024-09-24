from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from beanie import Document
 
class Register(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str
    pic_url: str

#the model saved to the database
class User(Document):
    username: str
    email: str
    password: str
    created_at: Optional[datetime] = None
    pic_url: Optional[str] = None