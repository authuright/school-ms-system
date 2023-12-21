from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
engine = create_engine('postgresql://authuright:authuright@0.0.0.0:5432/datacenter') 
session = scoped_session(sessionmaker(engine))
Base = declarative_base()
