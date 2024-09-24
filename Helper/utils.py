import re
from passlib.context import CryptContext


def isValidEmail(emial : str) ->bool:
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pattern , emial):
        return True
    return False 

passContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPasswod(password: str):
    return passContext.hash(password)

def verifyPassword(password : str, hashedPassword: str):
    return passContext.verify(password, hashedPassword)
