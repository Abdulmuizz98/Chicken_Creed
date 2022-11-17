#!/usr/bin/python3
""" Admin Module for Chicken Creed """
from models.base_model import BaseModel
from models import storage_t
import sqlalchemy
from sqlalchemy import relationship, Column, String, DateTime, ForeignKey


class Admin(BaseModel):
    """ The admin class"""
    if storage_t == 'db':
        __tablename__ = 'admins'
        user_id = Column(String(60), ForeignKey('users.id'))
        user = relationship('User', back_populates='admin')
    else:
        user_id = ""