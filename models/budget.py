#!/usr/bin/python3
""" Budget Module for Chicken Creed """
from models.base_model import BaseModel


class Budget(BaseModel):
    """ The budget class tracks buget subheads for a batch"""
    head = ""
    subhead = ""
    batch_id = ""
    cost = 0.00
    quantity = 0.00
    total_cost = 0.00
