from sqlalchemy import create_engine  # Fixed: removed 'create_all_engines'
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Point to our SQLite file
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/expenses.db"

# engine manages the connection to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Each instance of SessionLocal will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models
Base = declarative_base()

# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()