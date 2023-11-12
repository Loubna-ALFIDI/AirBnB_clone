#!/usr/bin/python3
"""FileStorage"""


from json import dump
from json import load
import os
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r",
                          encoding="utf-8") as jsonF:
                    json_data = load(jsonF)
                    for key, value in json_data.items():
                        if '.' in key:
                            class_name, obj_id = key.split('.')
                            class_obj = globals()[class_name]
                            new_instance = class_obj(**value)
                            self.new(new_instance)
                            self.__objects[key] = new_instance
            except FileNotFoundError:
                pass
