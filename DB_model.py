from db import Database
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime

db = Database()


class Model(db.Base):
    __tablename__ = "Model"
    Id = Column(Integer, primary_key=True)
    Link = Column(String)
    Date = Column(DateTime, default=datetime.datetime.utcnow)
    visited = Column(Boolean, default=False)


db.Base.metadata.create_all(db.engine, [Model.__table__])
db.session.commit()
