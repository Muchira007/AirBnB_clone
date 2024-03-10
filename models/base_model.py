#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """This is the class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """This initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the official string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the time to the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary with all key values of __dict__"""
        to_dict = self.__dict__.copy()
        to_dict["__class__"] = type(self).__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()
        return to_dict
