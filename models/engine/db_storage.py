#!/usr/bin/python3
"""
Contains the class DBStorage
"""

#import models
from models.base_model import BaseModel, Base
from models.user import User
from models.admin import Admin
from models.operator import Operator
from models.batch import Batch
from models.cost import Cost
from models.budget import Budget
from models.head import Head
from models.casualty import Casualty
from models.sale import Sale
from models.livestock import Livestock
from models.supplies import Supplies
from models.livestock_requisition import LivestockRequisition
from models.supplies_requisition import SuppliesRequisition
from models.request import Request
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
                "BaseModel": BaseModel, "User": User, "Admin": Admin,
                "Operator": Operator, "Batch": Batch, "Cost": Cost,
                "Budget": Budget, "Casualty": Casualty, "Sale": Sale,
                "Livestock": Livestock, "Supplies": Supplies,
                "Livestock_Requisition": LivestockRequisition,
                "Supplies_Requisition": SuppliesRequisition,
                "Request": Request, "Head": Head,
            }


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CC_MYSQL_USER = getenv('CC_MYSQL_USER')
        CC_MYSQL_PWD = getenv('CC_MYSQL_PWD')
        CC_MYSQL_HOST = getenv('CC_MYSQL_HOST')
        CC_MYSQL_DB = getenv('CC_MYSQL_DB')
        CC_ENV = getenv('CC_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CC_MYSQL_USER,
                                             CC_MYSQL_PWD,
                                             CC_MYSQL_HOST,
                                             CC_MYSQL_DB))
        if CC_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()