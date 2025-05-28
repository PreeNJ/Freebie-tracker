from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlite file will be created at ./db/development.db
DATABASE_URL = "sqlite:///db/development.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
