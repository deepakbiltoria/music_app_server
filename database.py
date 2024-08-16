from sqlalchemy import create_engine # this engine is required to connect our framework to postgreysql database
from sqlalchemy.orm import sessionmaker


""" Your original password is Misha@123.
Encode the @ as %40 """

DATABASE_URL = 'postgresql://postgres:Misha%40123@localhost:5432/musicapp'

engine = create_engine(DATABASE_URL) # here create engine returns Engine, this Engine is the starting point for sqlalchemy Application that need to connect to the database, this acts as a central source of connections to our database
#now the next thing we need to do is create a session

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine ) 

# sessionmaker this is a fuction that will create new session object when its called and this sessionlocal is the interface with which you interact the database in a transactional manner
#autocomit = false-> this setting means that the sqlAlchemy will not commit any transaction automatically, you will need to use transacntion.commit to commit transanction to te Database
#if autocomit = true-> it will commit each query/operation done to the DB will be imediately commited to the DB, which means you could not perform multiple query/operation in a single transanction
#autoFlush = False -> this autoflush determine whether the session should automatically flush pending changes to the database before each query
# when autoFlush = False , then sqlAlchemy wait to send the changes to the database untill we explicitly call Session.flush or Session.commit
#this important for performance as it reduces the round of trips to the database also give more control over when changes send to the databse
#which can be important for transanction integrity and consistancy

# Transanction means -> a request send to the database or an exchange that was done to the databse.
#this get_db method will yield a db when db a function needs it and close it when that function completes, this method will provide dependecy injection 
def get_db():
    db = sessionLocal() # here we get access to the database, db variable has the access to the database
    try:
        yield db
    finally:
        db.close()
