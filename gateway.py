from DB_model import Model
from db import Database


class Gateway():
    def __init__(self):
        self.db = Database()
        self.model = Model()

    def insert_in_db(self, link):
        self.db.session.add(Model(Link=link))
        self.db.session.commit()

    def check_if_in_db(self, link):
        db_link = self.db.session.query(Model.Link).filter(Model.Link == link).first()
        self.db.session.commit()
    
        if db_link is not None:
            return False
        return True
