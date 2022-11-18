#!/usr/bin/python3
""" User Module for Chicken Creed """
from models.base_model import BaseModel


class Wallet(BaseModel):
    """ The wallet class, tracks a chicken creed wallet"""
    state_id = ""
    name = ""
