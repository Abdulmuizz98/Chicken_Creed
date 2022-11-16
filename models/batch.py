#!/usr/bin/python3
""" Batch Module for Chicken Creed """
from models.base_model import BaseModel
# from datetime import datetime

class Batch(BaseModel):
    """ The batch class, models a batch of livestock production"""
    statuses = ["", "", ""]
    livestock_id = ""
    subscription_start_date = "" 
    subscription_end_date = "" 
    start_date = "" 
    end_date = "" 
    estimated_duration = ""
    subscription_unit_price = 0.00
    subscription_max_unit = 0
    status = statuses[0]
