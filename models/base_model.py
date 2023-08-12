#!/usr/bin/python3
"""
    base_model module
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialization of BaseModel instance """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at" or k == "created_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Overriden  __str__ method prints function """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returnsinstance in dict format """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
