import uuid
import bcrypt
from fastapi import  APIRouter, Depends, HTTPException 
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from sqlalchemy.orm import Session

from pydantic_schemas.user_login import UserLogin
#from database import db <- instead of this we will provide db via dependency injection

router = APIRouter()

@router.post('/signup', status_code = 201)
def signup_user(user: UserCreate, db: Session = Depends(get_db)): 
    # Depends provide Dependency injection
    #extract the data thats coming from requset
    print(user.name)
    print(user.email)
    print(user.password)

    #check if the user already exists in the db
    user_db = db.query(User).filter(User.email == user.email).first() 
    # if not user_db -> it evaluates to True if userdb is falsy mean is its either null,false,0,0.0,'',[],{},set()
    if user_db: 
        # return "User with this email already exists!"
        raise HTTPException(400, "User with this email already exists!") #400 status is for bad request
    #if user isnt in the db then add the user to the db
    hash_pass = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    user_db = User(id = str(uuid.uuid4()), name = user.name, email = user.email, password = hash_pass)
    db.add(user_db)
    db.commit()
    db.refresh(user_db) #here it refreshes the attributes on a particular instance, it refresh all fields in the the user_db and store it with correct value
    #otherwise if we dont use db.refresh then even though we have return user_db but it will return an empty dictionary {}
    return user_db

@router.post("/login")
def login_user(user : UserLogin, db : Session = Depends(get_db) ):

    #check if the email exists in db
    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        raise HTTPException(400, "Email does not exists")
    
    #check if password matches
    is_match = bcrypt.checkpw(user.password.encode(), user_db.password)

    if not is_match:
        raise HTTPException(400, "Incorrect Password")
    return user_db


