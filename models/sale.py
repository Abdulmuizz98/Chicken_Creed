#!/usr/bin/python3
""" Sale Module for Chicken Creed """
from models.base_model import BaseModel


class Sale(BaseModel):
    """ The sale class, models entries for the sale of livestock """
    batch_id = ""
    livestock_id = ""
    user_id = ""
    quantity = 0
    kg = 0.00
    price = 0.00
