from db import Database
from sqlalchemy import Column, Integer, String


db = Database()

class Model(db.Base):
    __tablename__ = "Model"
    Id = Column(Integer, primary_key=True)
    Link = Column(String)


db.Base.metadata.create_all(db.engine, [Model.__table__])
db.session.commit()
