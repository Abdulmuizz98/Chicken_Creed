#!/usr/bin/python3
""" Head Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Head(BaseModel, Base):
    """ The budget class models buget subheads for a batch"""
    if storage_t == 'db':
        __tablename__ = 'heads'
        name = Column(String(128), nullable=False)
    else:
        name = ""