from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DateTime import DateTime

Base = declarative_base()

class Customer(Base):
    '''the customer table'''
    __tablename__ = 'customer_table'
    customer_id = Column('customer_id', Integer, primary_key=True)
    name = Column('name', String)
    email = Column('email', String)
    phone = Column('phone', Integer)
    gender = Column('gender', CHAR)

    def __init__(self, customer_id, name, email, phone, gender):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender

class Sevices(Base):
    '''the services available'''
    __tablename__ = 'services_table'
    service_id = Column('service_id', Integer, primary_key=True)
    service_name = Column('service_name', String)
    description = Column('description', String)
    duration = Column('duration', DateTime)
    price = Column('price', Float)

    def __init__(self, service_id, service_name, description, duration, price):
        self.service_id = service_id
        self.service_name = service_name
        self.description = description
        self.duration = duration
        self.price = price

