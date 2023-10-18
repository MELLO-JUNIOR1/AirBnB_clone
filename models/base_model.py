#!/usr/bin/env python3
"""
    Module for Base Model
"""
import uuid
from datetime import datetime
import models


class BaseModel(object):
    """
       a class BaseModel that defines all common
       attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:

            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])

            if "__class__" in kwargs:
                del kwargs["__class__"]

            for key, value in kwargs.items():              
             setattr(self, key, value)

    def __str__(self):
        """
            string representation of
            the Object
        """

        name = self.__class__.__name__
        dic = self.__dict__
        id = self.id
        return "[{}] ({}) {}".format(name, id, dic)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """

        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic
