#!/usr/bin/python3
""" Livestock_Requisition Module for Chicken Creed """
from models.request import Request
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

class Livestock_Requisition(Request):
    """ The livestock_requisition class, helps track movement
    of livestock to operators """
    if storage_t == 'db':
        __table__ = 'livestock_requisitions'
        livestock_id = Column(String(60), ForeignKey('livestocks.id'), nullable=False)
        livestock = relationship('Livestock')
        operator_id = Column(String(60), ForeignKey('operators.id'), nullable=False)
        operator = relationship('Operator')
        operator_id = Column(String(60), ForeignKey('operators.id'), nullable=False)
        operator = relationship('Operator')
        request_id = Column(String(60), ForeignKey('requests_id'), nullable=False)
        request = relationship('Request', back_populates='livestock_requisition')
        quantity = Column(Integer, nullable=False)
    else:
        livestock_id = ""
        operaor_id = ""
        batch_id = ""
        request_id = ""
        quantity = 0