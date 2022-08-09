#!/usr/bin/env python3

from datetime import datetime
import models
import uuid

''' Define class BaseModel'''


class BaseModel:
    """creating Basemodel class"""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        '''updated at the current date time'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns all dict containing all keys/values of instance'''
        model_dict = dict(self.__dict__)
        tym = "%Y-%m-%dT%H:%M:%S.%f"
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.strftime(tym)
        model_dict['updated_at'] = self.updated_at.strftime(tym)
        return model_dict
