#!/usr/bin/python3
"""contains file storage class"""


import models
import json
from models.user import User


class FileStorage():
    """"""
    __file_path = "model_file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for key, val in FileStorage.__objects.items():
            my_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
