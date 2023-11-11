#!/usr/bin/python3
'''BaseModel'''


from uuid import uuid4
from datetime import datetime
from models import FileStorage
from models import storage

class BaseModel:
    '''base model'''
    def __init__(self, *args, **kwargs):
        '''init'''
        if kwargs:
            del kwargs['__class__']
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage().new(self)
    
    def save(self):
        '''save'''
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        '''to dict'''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict
    
    def __str__(self):
        '''str'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
