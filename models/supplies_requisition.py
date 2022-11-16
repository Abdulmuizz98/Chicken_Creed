#!/usr/bin/python3
""" Supplies_Requisition Module for Chicken Creed """
from models.request import Request


class Supplies_Requisition(Request):
    """ The supplies_requisition class, helps track movement of supplies to operators """
    supplies_id = ""
    quantity = ""
    operaor_id = ""
    batch_id = ""
    admin_id = ""
    date = ""
    time = ""
