from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@47.98.161.129/edu?charset=utf8')

DbSession = sessionmaker(bind=engine)

session = DbSession()

Base = declarative_base(bind=engine)
