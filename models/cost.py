#!/usr/bin/python3
""" Cost Module for Chicken Creed """
from models.request import Request
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship


class Cost(Request, Base):
    """ The cost class models expenditure on a batch carried out by an admin"""
    if storage_t == 'db':
        __table__ = 'costs'
        batch_id = Column(String(60), ForeignKey('batches.id'))
    budget_id = ""
    batch_id = ""
    admin_id = ""
    description = ""
    cost = 0.00
    quantity = 0.00
    total_cost = 0.00
