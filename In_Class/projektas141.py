import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Sukursime savo duomenu baze
engine = create_engine('sqlite:///projektai.db')

# Sukursme savo bazes modeli
Base = declarative_base()

# Apibreziame klase "Projektas"
class Projektas(Base):
    __tablename__ = 'Projektas'
    id = Column(Integer, primary_key=True)
    name = Column('Pavadinimas', String)
    price = Column('Kaina', Float)
    created_date = Column('Sukurimo_data', DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.created_date}'
    
# Sukuriamas lenteles pagal modeli
Base.metadata.create_all(engine)