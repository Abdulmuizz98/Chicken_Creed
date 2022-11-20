#!/usr/bin/python3
""" Casualty Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import relationship

class Casualty(BaseModel, Base):
    """ The casualty class, models a casualty report by operators """
    if storage_t == 'db':
        __tablename__ = 'casualties'
        description = Column(String(1024), nullable=False)
        batch_id = Column(String(60), ForeignKey('batches.id'),nullable=False)
        request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)
        operator_id = Column(String(60), ForeignKey('operators.id'), nullable=False)
        livestock_id = Column(String(60), ForeignKey('livestocks.id'), nullable=False)
        request = relationship('Request', back_populates='casualty')
        operator = relationship('Operator')
        livestock = relationship('Livestock')
        casualty_count = Column(Integer, nullable=False)
    else:
        description = ""
        batch_id = ""
        request_id = ""
        operator_id = ""
        livestock_id = ""
        casualty_count = 0
