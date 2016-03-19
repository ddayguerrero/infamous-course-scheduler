from sqlalchemy import MetaData
from app import engine, Base
# Import session
from sqlalchemy.orm import sessionmaker, scoped_session

def start_session():
	db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
	metadata = MetaData()

	Base.query = db_session.query_property()

	return db_session
