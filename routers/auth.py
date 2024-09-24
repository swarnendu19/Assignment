from fastapi import APIRouter, Response, status,HTTPException
from config.settings import settings
from models.user import UserResponse, Register, User
from Helper.utils import isValidEmail, hashPasswod
from datetime import datetime, timezone


router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

#Reister
@router.post('/register', status_code= status.HTTP_201_CREATED, response_model=UserResponse)
async def createUser(payload : Register):
    if not isValidEmail(payload.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Email"
        )
    userExist = await User.find_one(User.username == payload.username)
    emailExist = await User.find_one(User.email == payload.email)
    if userExist or emailExist:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail= 'Account Already Exist'
        )
    newUser = User(
        username=payload.username,
        email= payload.email.lower(),
        password=hashPasswod(payload.password),
        created_at=datetime.now(timezone.utc)
    )
    await newUser.create()
    resUser = UserResponse(
        username=newUser.username,
        email = newUser.email,
        pic_url=str(newUser.pic_url)
    )
    return resUser



#Sign IN 
 