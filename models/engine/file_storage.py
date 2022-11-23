#!/usr/bin/python3
import json
from models.base_model import BaseModel
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

        dictio = FileStorage.__objects
        dict_obj = {obj: dictio[obj].to_dict() for obj in dictio.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """loads obj from a path file"""

        try:
            with open(FileStorage.__file_path, "r") as f:
                dic_obj = json.load(f)
                for obj in dic_obj.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
