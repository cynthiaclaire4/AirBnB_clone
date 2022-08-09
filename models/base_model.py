from msilib.schema import Class
import string
from uuid import uuid4
from datetime import datetime
import uuid

''' Define class BaseModel'''

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime
    updated_at = datetime

    '''intializing the class'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = created_at

def __str__(self):
    """String representation of the BaseModel class"""
    return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updated at the current date time'''
        self.updated_at = datetime.now()

    def to_dict(self)
    '''returns all dict containing all keys/values of instance'''
    new_dict = self.__dict__.copy()
    return new_dict

    





        





