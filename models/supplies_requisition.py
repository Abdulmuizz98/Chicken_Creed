#!/usr/bin/python3
""" Supplies_Requisition Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class SuppliesRequisition(BaseModel):
    """ The supplies_requisition class, helps track movement
    of supplies to operators """
    if storage_t == 'db':
        __tablename__ = 'supplies_requisitions'
        supplies_id = Column(String(60), ForeignKey('suppliess.id'), nullable=False)
        supplies = relationship('supplies')
        operator_id = Column(String(60), ForeignKey('operators.id'), nullable=False)
        operator = relationship('Operator')
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        request_id = Column(String(60), ForeignKey('requests_id'), nullable=False)
        request = relationship('Request', back_populates='supplies_requisition', cascade="all, delete, delete-orphan")
        quantity = Column(Integer, nullable=False)
    else:
        supplies_id = ""
        operaor_id = ""
        batch_id = ""
        request_id = ""
        quantity = 0