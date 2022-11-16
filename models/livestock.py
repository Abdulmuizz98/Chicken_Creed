#!/usr/bin/python3
""" Livestock Module for Chicken Creed """
from models.base_model import BaseModel


class Livestock(BaseModel):
    """ The livestock class, models the stock of livestock available per purchase"""
    cost_id = ""
    batch_id = ""
    livestock_type = ""
    quantity = 0
    requisitioned = 0
