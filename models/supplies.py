#!/usr/bin/python3
""" Supplies Module for Chicken Creed """
from models.base_model import BaseModel


class Supplies(BaseModel):
    """ The supplies class, models the stock of supplies
    available per purchase"""
    cost_id = ""
    batch_id = ""
    supplies_type = ""
    quantity = 0
    requisitioned = 0
