#!/usr/bin/python3
""" Budget Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship


class Budget(BaseModel, Base):
    """ The budget class models buget subheads for a batch"""
    if storage_t == 'db':
        __table__ = 'budgets'
        batch_id = Column(String(60), ForeignKey('batches.id'))
        head_id =  Column(String(60), ForeignKey('heads_id'), nullable=False)
        head = relationship('Budget')
        name = Column(String(128), nullable=False)
        unit_cost = Column(Numeric, nullable=False)
        quantity = Column(Numeric)
        unit_name = Column(String(20))
        total_cost = Column(Numeric, nullable=False)
    else:
        head_id = ""
        batch_id = ""
        unit_cost = 0.00
        quantity = 0.00
        unit_name = ""
        total_cost = 0.00