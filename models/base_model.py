#!/usr/bin/python3
"""
This module defines BaseModel - a base class for all
Chiken Creed project objects
"""
from uuid import uuid4
from datetime import datetime
from models import storage_t
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

if storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    Definition of the BaseModel class
    """
    if storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    datetime_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    datetime_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                from models import storage
                self.id = str(uuid4())
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the BaseModel object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method that sets the time object was updated
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Generates a dictionary representation of the object
        """
        dic = {}
        dic.update(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dic:
            del dic['_sa_instance_state']
        return dic

    def delete(self):
        """
        Delete the current instance(self) from storage
        """
        storage.delete(self)
