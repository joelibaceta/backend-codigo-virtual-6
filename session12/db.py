from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine("mysql+pymysql://root:rootcodigo@localhost/usersdb")

Base = declarative_base()

Session = sessionmaker(bind=engine)