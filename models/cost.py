#!/usr/bin/python3
""" Cost Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Cost(BaseModel, Base):
    """ The cost class models expenditure on a batch carried out by an admin"""
    if storage_t == 'db':
        __tablename__ = 'costs'
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        head_id =  Column(String(60), ForeignKey('heads.id'), nullable=False)
        head = relationship('Head')
        budget_id = Column(String(60), ForeignKey('budgets.id'))
        budget = relationship('Budget')
        request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)
        request = relationship('Request', back_populates='cost')
        livestock = relationship('Livestock', back_populates='cost')
        supplies = relationship('Supplies', back_populates='cost') # its a one don't be deceived by s in supplies
        description = Column(String(1024))
        unit_cost = Column(Float, nullable=False)
        quantity = Column(Float)
        total_cost = Column(Float, nullable=False)
    else:
        head_id = ""
        budget_id = ""
        batch_id = ""
        request_id = ""
        description = ""
        unit_cost = 0.00
        quantity = 0.00
        total_cost = 0.00
