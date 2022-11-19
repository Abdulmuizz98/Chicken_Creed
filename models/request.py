#!/usr/bin/python3
""" Request Module for Chicken Creed """
from models.base_model import BaseModel, Base
import enum
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, Enum, Table
from sqlalchemy.orm import relationship


class Status(enum.Enum):
    """Enumerated type to track the status of requests."""
    RAISED = 1
    PENDING = 2
    ACCEPTED = 3
    SPENT = 4

if storage_t == 'db':
    request_admin =  Table('request_admin', Base.metadata,
                          Column('request_id', String(60),
                                 ForeignKey('requests.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('admin_id', String(60),
                                 ForeignKey('admins.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))
class Request(BaseModel, Base):
    """ The request class, models request and requisitions needing approval """
    if storage_t == 'db':
        __tablename__ = 'requests'
        batch_id = Column(String(60), ForeignKey('batches.id'), nullable=False)
        status = Column(Enum(Status), nullable=False, default=Status.RAISED)
        casualty = relationship('Casualty', uselist=False, back_populates='request')
        cost = relationship('Cost', uselist=False, back_populates='request')
        # batch = relationship('Batch', uselist=False, back_populates='request') # for one to one batch matching
        livestock_requisition = relationship('LivestockRequisition', uselist=False, back_populates='request')
        supplies_requisition = relationship('SuppliesRequisition', uselist=False, back_populates='request')
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship('User') # raised_by_user_id  (many to one)
        admins = relationship("Admin", secondary='request_admin', back_populates='request_admin') # sign_by_admin_ids (many to many)
    else:
        batch_id = ""
        status = Status.RAISED
        # casualty = ""
        # cost = ""
        # livestock_requisition = ""
        # supplies_requisition = ""
        user_id = ""

    if storage_t != 'db':
        def instance_list_helper(self, Obj):
            """Gets a list from storage"""
            from models import storage
            obj_list = []
            all_obj = storage.all(Obj)
            for obj in all_obj.values():
                if obj.request_id == self.id:
                    obj_list.append(obj)
            return obj_list

        @property
        def admins(self):
            """getter attribute returns the list of Admin instances"""
            from models.admin import Admin
            return self.instance_list_helper(Admin)
