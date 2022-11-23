#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
class BaseModel with public attributes
"""


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initial method"""

        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k == "id":
                    self.id = v
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation
        """
        name = self.__class__.__name__
        return("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """
        saves updating time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dictio = self.__dict__.copy()
        dictio["__class__"] = self.__class__.__name__
        dictio["created_at"] = self.created_at.isoformat()
        dictio["updated_at"] = self.updated_at.isoformat()

        return dictio
