from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///URL.db', connect_args={'timeout': 15}) 
        self.sessionM = sessionmaker(bind=self.engine)
        self.session = self.sessionM()
        self.session.autoflush = True
