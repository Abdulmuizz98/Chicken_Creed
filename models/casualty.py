#!/usr/bin/python3
""" Casualty Module for Chicken Creed """
from models.request import Request


class Casualty(Request):
    """ The casualty class, models a casualty report by operators """
    operator_id = ""
    batch_id = ""
    casualty_count = 0
    description = ""
