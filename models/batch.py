#!/usr/bin/python3
""" Batch Module for Chicken Creed """
from models.base_model import BaseModel, Base
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

if storage_t == 'db':
    batch_user = Table('batch_user', Base.metadata,
                          Column('batch_id', String(60),
                                 ForeignKey('batches.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('user_id', String(60),
                                 ForeignKey('users.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

    batch_operator = Table('batch_operator', Base.metadata,
                          Column('batch_id', String(60),
                                 ForeignKey('batches.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('operator_id', String(60),
                                 ForeignKey('operators.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

class Batch(BaseModel, Base):
    """ The batch class, models a batch of livestock production"""
    if storage_t == 'db':
        __tablename__ = 'batches'
        subscription_start_date = Column(DateTime, nullable=False)
        subscription_end_date = Column(DateTime, nullable=False)
        start_date = Column(DateTime, nullable=False)
        end_date = Column(DateTime, nullable=False)
        estimated_duration = Column(Integer, nullable=False, default=60)
        subscription_unit_price = Column(Float, nullable=False)
        subscription_max_unit = Column(Integer, nullable=False)
        request_id = Column(String(60), ForeignKey('requests.id'), nullable=False) # for one to one request matching
        request = relationship('Request_req', back_populates='batch', cascade="all, delete, delete-orphan") # for one to one request matching
        requests = relationship('Request')
        livestocks = relationship('Livestock')
        livestock_requisitions = relationship('LivestockRequisition')
        sales = relationship('Sale')
        costs = relationship('Cost')
        budgets = relationship('Budget')
        supplies = relationship('Supplies')
        supplies_requisitions = relationship('SuppliesRequisition')
        casualties = relationship('Casualty')
        operators = relationship('Operator', secondary='batch_operator', back_populates='batch_operator') # many to many
        subscribers = relationship('User', secondary='batch_user', back_populates='batch_user') # many to many 
    else:
        subscription_start_date = ""
        subscription_end_date = ""
        start_date = ""
        end_date = ""
        estimated_duration = ""
        subscription_unit_price = 0.00
        subscription_max_unit = 0
        subscriber_user_ids = [] # many to many
        # method for inventory
        # method for units subscribed
        # method for pool
        # method for livestock_types
        # method for revenue
        # method for cost

    if storage_t != 'db':
        def instance_list_helper(self, Obj):
            """Gets a list from storage"""
            from models import storage
            obj_list = []
            all_obj = storage.all(Obj)
            for obj in all_obj.values():
                if obj.batch_id == self.id:
                    obj_list.append(obj)
            return obj_list

        @property
        def requests(self):
            """getter attribute returns the list of Request instances"""
            from models.request import Request
            return self.instance_list_helper(Request)

        @property
        def livestocks(self):
            """getter attribute returns the list of Livestock instances"""
            from models.livestock import Livestock
            return self.instance_list_helper(Livestock)

        @property
        def operators(self):
            """getter attribute returns the list of Operator instances"""
            from models.operator import Operator
            return self.instance_list_helper(Operator)

        @property
        def sales(self):
            """getter attribute returns the list of Sale instances"""
            from models.sale import Sale
            return self.instance_list_helper(Sale)

        @property
        def costs(self):
            """getter attribute returns the list of Cost instances"""
            from models.cost import Cost
            return self.instance_list_helper(Cost)

        @property
        def budget(self):
            """getter attribute returns the list of Budget instances"""
            from models.budget import Budget
            return self.instance_list_helper(Budget)

        @property
        def supplies(self):
            """getter attribute returns the list of Supplies instances"""
            from models.supplies import Supplies
            return self.instance_list_helper(Supplies)

        @property
        def casualties(self):
            """getter attribute returns the list of Casualty instances"""
            from models.casualty import Casualty
            return self.instance_list_helper(Casualty)

        @property
        def subscribers(self):
            """getter attribute returns the list of User instances"""
            from models.user import User
            return self.instance_list_helper(User)