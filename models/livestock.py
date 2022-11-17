#!/usr/bin/python3
""" Livestock Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Livestock(BaseModel):
    """ The livestock class, models the stock of
    livestock available per purchase"""
    if storage_t == 'db':
        __table__ = 'batches'
        batch_id = Column(String(60), ForeignKey('batches.id'))
    cost_id = ""
    batch_id = ""
    livestock_type = ""
    quantity = 0
    requisitioned = 0
