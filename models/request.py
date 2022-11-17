#!/usr/bin/python3
""" Request Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship



class Request(BaseModel, Base):
    """ The request class, models request and requisitions needing approval """
    if storage_t == 'db':
        __table__ = 'requests'
        batch_id = Column(String(60), ForeignKey('batches.id'))
        casualty_id = relationship('Casualty', uselist=False, back_populates='request')

    else:
        statuses = ["", "", ""]
        sign_admin_id = []
        status = statuses[0]
