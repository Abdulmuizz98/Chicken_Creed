#!/usr/bin/python3
""" Batch Module for Chicken Creed """
from models.request import Request
# from datetime import datetime


class Batch(Request):
    """ The batch class, models a batch of livestock production"""
    statuses = ["", "", ""]
    livestock_ids = ""
    subscription_start_date = ""
    subscription_end_date = ""
    start_date = ""
    end_date = ""
    estimated_duration = ""
    subscription_unit_price = 0.00
    subscription_max_unit = 0
    operator_ids = []
    admin_ids = []
    sale_ids = []
    cost_ids = []
    budget_ids = []
    supplies_ids = []
    casualty_ids = []
    subscription_user_ids = []
    # method for inventory
    # method for units subscribed
    # method for pool
    # method for livestock_types
    # method for revenue
    # method for cost
