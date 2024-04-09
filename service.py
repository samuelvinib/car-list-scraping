# service.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Car
import datetime
import uuid

class DatabaseService:
    def __init__(self):
        engine = create_engine('mysql://user:my-secret-pw@localhost/laravel')
        self.Session = sessionmaker(bind=engine)

    def save_car(self, name, fipe_code, price):
        session = self.Session()
        carro = Car(name=name, fipe_code=fipe_code, price=price)
        session.add(carro)
        session.commit()
        session.close()
