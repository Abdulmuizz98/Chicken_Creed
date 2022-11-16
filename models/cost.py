#!/usr/bin/python3
""" Cost Module for Chicken Creed """
from models.base_model import BaseModel


class Cost(BaseModel):
    """ The cost class models expenditure on a batch carried out by an admin"""
    head = ""
    subhead = ""
    batch_id = ""
    admin_id = ""
    cost = 0.00
    quantity = 0.00
    total_cost = 0.00
