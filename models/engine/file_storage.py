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

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

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
        from models.casualty import Casualty
        from models.sale import Sale
        from models.livestock import Livestock
        from models.supplies import Supplies
        from models.livestock_requisition import Livestock_Requisition
        from models.supplies_requisition import Supplies_Requisition
        from models.request import Request

        classes = {
                        "BaseModel": BaseModel, "User": User, "Admin": Admin,
                        "Operator": Operator, "Batch": Batch, "Cost": Cost,
                        "Budget": Budget, "Casualty": Casualty, "Sale": Sale,
                        "Livestock": Livestock, "Supplies": Supplies,
                        "Livestock_Requisition": Livestock_Requisition,
                        "Supplies_Requisition": Supplies_Requisition,
                        "Request": Request,
                        
                  }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
