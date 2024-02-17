import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

# Retrieve environment variables
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_host = os.environ.get('POSTGRES_HOST')  # Use the service name from docker-compose
db_port = os.environ.get('POSTGRES_PORT')
db_name = os.environ.get('POSTGRES_DB')
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


# debug
print(f"db_user: {db_user}")
print(f"db_password: {db_password}")
print(f"db_host: {db_host}")
print(f"db_port: {db_port}")
print(f"db_name: {db_name}")
print(f"Database URL: {db_url}")
engine = create_engine(db_url)
try:
    conn = engine.connect()
    print("Database connection successful!")
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")



session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()