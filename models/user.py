#!/usr/bin/python3
""" User Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ The user class models a member of the cooperative"""
    if storage_t == 'db':
        __tablename__ = 'users'
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        phone = Column(String(20), nullable=True)
        address = Column(String(128), nullable=True)
        admin = relationship('Admin', uselist=False, back_populates='user')
        operator = relationship('Operator', uselist=False, back_populates='user')
    else:
        first_name = ""
        last_name = ""
        email = ""
        password = ""
        phone = ""
        address = ""