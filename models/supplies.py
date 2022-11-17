#!/usr/bin/python3
""" Supplies Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

class Supplies(BaseModel, Base):
    """ The supplies class, models the stock of supplies
    available per purchase"""
    if storage_t == 'db':
        __table__ = 'supplies'
        batch_id = Column(String(60), ForeignKey('batches.id'))
    cost_id = ""
    batch_id = ""
    supplies_type = ""
    quantity = 0
    requisitioned = 0
