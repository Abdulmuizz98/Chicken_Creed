#!/usr/bin/python3
""" Operator Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Operator(BaseModel, Base):
    """ The operator class"""
    if storage_t == 'db':
        __tablename__ = 'operators'
        user_id = Column(String(60), ForeignKey('users.id'))
        user = relationship('User', back_populates='operator')
    else:
        user_id = ""