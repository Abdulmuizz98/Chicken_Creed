#!/usr/bin/python3
""" User Module for Chicken Creed """
from models.base_model import BaseModel


class User(BaseModel):
    """ The user class models a member of the cooperative"""
    admin_id = ""
    operator_id = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
