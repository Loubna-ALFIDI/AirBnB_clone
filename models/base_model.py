#!/usr/bin/python3
"""Base Model
Usage:
python3 models/base_model.py
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        INIT

        Args:

        args: list

        kwargs: dict

        Return: None

        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, time_format)
            self.updated_at = datetime.strptime(self.updated_at, time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        storage.new(self)

    def __str__(self):
        """
        STR

        Return: str
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        save

        Return: None
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict

        Return: dict

        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict
