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
        cost_id = relationship('Cost', uselist=False, back_populates='request')
        livestock_requisition_id = relationship('Livestock_Requisition', uselist=False, back_populates='request')

    else:
        statuses = ["", "", ""]
        sign_admin_id = []
        status = statuses[0]
        raised_by_id = ""
