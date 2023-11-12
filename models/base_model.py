#!/usr/bin/python3
"""Base Model
Usage:
python3 models/base_model.py
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        INIT

        Args:

        args: list

        kwargs: dict

        Return: None

        """
        if kwargs:
            del kwargs["__class__"]
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
        models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        to_dict

        Return: dict

        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict
