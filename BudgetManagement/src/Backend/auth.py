from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict  
from jose import jwt, JWTError
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/auth', 
    tags=['auth']
)

SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')  
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')  

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_user(create_user_request: CreateUserRequest, db: Session = Depends(get_db)):
    hashed_password = bcrypt_context.hash(create_user_request.password)
    create_user_model = Users(username=create_user_request.username, hashed_password=hashed_password)
    db.add(create_user_model)
    db.commit()
    return JSONResponse(content={"message": "User created successfully"})


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestFormStrict = Depends(), 
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    
    return {'access_token': token, 'token_type': 'bearer'}


def authenticate_user (username: str, password: str, db):
    user = db.query (Users) . filter (Users. username == username) .first ()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False 
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}  # Fixed the typos in 'user_id'
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)  # Fixed the typo in 'algorithm'


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user.'
            )
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )
    

