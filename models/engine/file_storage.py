#!/usr/bin/python3
import json
from models.base_model.py import BaseModel
"""
serializes to JSON and deserializes from JSON
"""


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all dictionaries"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects"""

        obje = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obje, obj.id)] = obj

    def save(self):
        """serialize __objects to json"""


