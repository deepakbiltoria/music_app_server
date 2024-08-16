 
from fastapi import FastAPI 
from routes import auth
from models.base import Base
from database import engine

app = FastAPI()

app.include_router(auth.router, prefix = '/auth')



Base.metadata.create_all(engine)  #now the next thing we need to do is tell sqlalchemy to find all the classes that extend BASE so that it can create table
#based on the information that is present in the class othetrwise it wouldnt know what classes to take and create tables off


