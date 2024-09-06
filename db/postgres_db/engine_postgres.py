import sqlalchemy
from sqlalchemy.orm import sessionmaker

from db.postgres_db.model import Base

DSN = 'postgresql://postgres:5814@localhost:5432/blogs_db'
engine = sqlalchemy.create_engine(DSN)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


# def create_tables():
#     Base.metadata.drop_all(engine)
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#     Base.metadata.create_all(engine)
#
#
# create_tables()
