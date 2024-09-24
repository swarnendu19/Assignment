from fastapi import APIRouter, Response, status,HTTPException, Depends
from config.settings import settings
from models.user import UserResponse, Register, User, Login
from Helper.utils import isValidEmail, hashPasswod, verifyPassword
from datetime import datetime, timezone, timedelta
from Helper import oauth2

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

@router.post('/login')
async def login(payload: Login, response: Response):
    # Authenticate the user
    user = await User.find_one(User.username == payload.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    if not verifyPassword(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect username or password'
        )
    # Creating access token and refresh token
    access_token = oauth2.create_access_token(
        data={"sub": str(user.id)},  
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    )

    refresh_token = oauth2.create_access_token(
        data={"sub": str(user.id)},   
        expires_delta=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN)
    )
 
    response.set_cookie('access_token', access_token, ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('refresh_token', refresh_token,
                        REFRESH_TOKEN_EXPIRES_IN * 60, REFRESH_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('logged_in', 'True', ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, False, 'lax')

    return {'status': 'success', 'access_token': access_token}



 