# now we will extend our User class with Base, because we need to extend User class with some thing from sqlalchemy so that
# our sqlalchemy get to know that User is a tabe that the programmer would like to create if it already dosent exist

from models.base import Base
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary



class User(Base):
    __tablename__ = "users"

    #if User is the table than all of its variables are Columns , and here this Column class comes from sqlalchemy
    id = Column(TEXT, primary_key = True) #Variable type inside Column(TEXT) will always be imported from sqlalchemy
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)
