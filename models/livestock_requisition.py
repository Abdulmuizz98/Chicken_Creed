#!/usr/bin/python3
""" Livestock_Requisition Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class LivestockRequisition(BaseModel, Base):
    """ The livestock_requisition class, helps track movement
    of livestock to operators """
    if storage_t == 'db':
        __tablename__ = 'livestock_requisitions'
        livestock_id = Column(String(60), ForeignKey('livestocks.id'), nullable=False)
        livestock = relationship('Livestock')
        operator_id = Column(String(60), ForeignKey('operators.id'), nullable=False)
        operator = relationship('Operator')
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)
        request = relationship('Request', back_populates='livestock_requisition', cascade="all, delete, delete-orphan")
        quantity = Column(Integer, nullable=False)
    else:
        livestock_id = ""
        operaor_id = ""
        batch_id = ""
        request_id = ""
        quantity = 0