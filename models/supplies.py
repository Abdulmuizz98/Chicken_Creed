#!/usr/bin/python3
""" Supplies Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Supplies(BaseModel, Base):
    """ The supplies class, models the stock of supplies
    available per purchase"""
    if storage_t == 'db':
        __tablename__ = 'supplies'
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        supplies_type = Column(String(128), nullable=False)
        cost_id = Column(String(60), ForeignKey('costs.id'), nullable=False)
        cost = relationship('Cost', back_populates='supplies')
        quantity = Column(Integer, nullable=False)
    else:
        batch_id = "" 
        supplies_type = ""
        cost_id = "" # one to one mapping
        quantity = 0

    if storage_t != 'db':
        def instance_list_helper(self, Obj):
            """Gets a list from storage"""
            from models import storage
            obj_list = []
            all_obj = storage.all(Obj)
            for obj in all_obj.values():
                if obj.supplies_id == self.id:
                    obj_list.append(obj)
            return obj_list

        @property
        def requisitions(self):
            """getter attribute returns the list of SuppliesRequisition instances"""
            from models.supplies_requisition import SuppliesRequisition
            return self.instance_list_helper(SuppliesRequisition)
