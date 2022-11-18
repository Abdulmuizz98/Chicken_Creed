#!/usr/bin/python3
"""
Module containing FileStorage object definition
"""
import json


class FileStorage:
    """
    Definition of the FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
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

        classes = {
                        "BaseModel": BaseModel, "User": User, "Admin": Admin,
                        "Operator": Operator, "Batch": Batch, "Cost": Cost,
                        "Budget": Budget, "Casualty": Casualty, "Sale": Sale,
                        "Livestock": Livestock, "Supplies": Supplies,
                        "Livestock_Requisition": LivestockRequisition,
                        "Supplies_Requisition": SuppliesRequisition,
                        "Request": Request, "Head": Head,
                  }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()