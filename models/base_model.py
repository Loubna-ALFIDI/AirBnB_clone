#!/usr/bin/python3
'''BaseModel'''


from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''base model'''
    def __init__(self):
        '''init'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def save(self):
        '''save'''
        self.updated_at = datetime.now()
    
    def to_dict(self):
        '''to dict'''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
    
    def __str__(self):
        '''str'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
