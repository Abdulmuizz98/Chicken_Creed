#!/usr/bin/python3
""" Livestock Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t, storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

class Livestock(BaseModel, Base):
    """ The livestock class, models the stock of
    livestock available per purchase"""
    if storage_t == 'db':
        __table__ = 'livestocks'
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        livestock_type = Column(String(128), nullable=False)
        cost_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        cost = relationship('Cost', back_populates='livestock')
        quantity = Column(Integer, nullable=False)
        price = Column(Numeric, nullable=False )
    else:
        cost_id = "" # one to one mapping
        batch_id = "" 
        livestock_type = ""
        quantity = 0
        price = 0.00

    if storage_t != 'db':
        def instance_list_helper(self, Obj):
            """Gets a list from storage"""
            obj_list = []
            all_obj = storage.all(Obj)
            for obj in all_obj.values():
                if obj.livestock_id == self.id:
                    obj_list.append(obj)
            return obj_list

        @property
        def requisitions(self):
            """getter attribute returns the list of Livestock_ instances"""
            from models.livestock_requisition import LivestockRequisition
            return self.instance_list_helper(LivestockRequisition)