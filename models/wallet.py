#!/usr/bin/python3
""" User Module for Chicken Creed """
from models.base_model import BaseModel


class User(BaseModel):
    """ The user class, contains state ID and name """
    state_id = ""
    name = ""
