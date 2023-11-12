#!/usr/bin/python3
"""FileStorage"""


from json import dump
from json import load
from models.user import User


class FileStorage:
    """FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """all"""
        return self.__objects

    def new(self, obj):
        """new"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save"""
        dobj = {}
        for key, val in self.__objects.items():
            dobj[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as jsonF:
            dump(dobj, jsonF)

    def reload(self):
        """reload"""
        from models.base_model import BaseModel

        definclass = {'BaseModel': BaseModel, 'User': User}
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as jsonF:
                dobj = load(jsonF)
                for key, val in dobj.items():
                    self.__objects[key] = definclass[val['__class__']](**val)
        except FileNotFoundError:
            pass
