#!/usr/bin/python3
""" Livestock_Requisition Module for Chicken Creed """
from models.request import Request


class Livestock_Requisition(Request):
    """ The livestock_requisition class, helps track movement of livestock to operators """
    livestock_id = ""
    quantity = ""
    operaor_id = ""
    batch_id = ""
    admin_id = ""
    date = ""
    livestock_type = ""
