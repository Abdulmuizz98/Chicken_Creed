#!/usr/bin/python3
""" Sale Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Sale(BaseModel, Base):
    """ The sale class, models entries for the sale of livestock """
    if storage_t == 'db':
        __tablename__ = 'sales'
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        livestock_id =  Column(String(60), ForeignKey('livestocks.id'), nullable=False)
        livestock = relationship('Livestock')
        user_id =  Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship('User')
        quantity = Column(Integer, nullable=False)
        kg = Column(Float, nullable=False)
        total_price = Column(Float, nullable=False)
        
    else:
        batch_id = ""
        livestock_id = "" # many to one
        user_id = "" # many to one
        quantity = 0
        kg = 0.00
        total_price = 0.00