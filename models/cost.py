#!/usr/bin/python3
""" Cost Module for Chicken Creed """
from models.request import Request


class Cost(Request):
    """ The cost class models expenditure on a batch carried out by an admin"""
    budget_id = ""
    batch_id = ""
    admin_id = ""
    description = ""
    cost = 0.00
    quantity = 0.00
    total_cost = 0.00
