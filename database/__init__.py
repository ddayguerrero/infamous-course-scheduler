from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from app import engine
# Import session
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

def start_session():
	db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
	metadata = MetaData()

	Base.query = db_session.query_property()

	return db_session
