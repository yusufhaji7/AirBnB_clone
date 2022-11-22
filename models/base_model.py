#!/usr/bin/python3
import uuid
from datetime import datetime
"""
class BaseModel with public attributes
"""


class BaseModel:

    def __init__(self):
        """initial method"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string representation
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,
            self.id, self.__dict__))

    def save(self):
        """
        saves updating time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values 
        of __dict__ of the instance
        """
        dictio = self.__dict__.copy()
        dictio["__class__"] = self.__class.__name__
        dictio["created_at"] = self.created_at.isoformat()
        dictio["updated_at"] = self.updated_at.isoformat()

        return dictio
