#!/usr/bin/python3
""" Request Module for Chicken Creed """
from models.base_model import BaseModel


class Request(BaseModel):
    """ The request class, models request and requisitions needing approval """
    statuses = ["", "", ""]
    signatories = []
    status = statuses[0]
