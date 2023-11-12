#!/usr/bin/python3
"""Unit tests for FileStorage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage"""

    def setUp(self):
        """Setting up the test cases"""
        super().setUp()
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel." + self.instance.id

    def test_all(self):
        """Test all"""
        self.assertTrue(hasattr(storage, "all"))

    def test_new(self):
        """Test new"""
        self.assertTrue(hasattr(storage, "new"))

    def test_reload(self):
        """Test reload"""
        self.assertTrue(hasattr(storage, "reload"))

    def test_all_methode(self):
        """test all methode"""
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new_methode(self):
        """test new methode"""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all().keys())

    def test_save_method(self):
        """Test the save() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        expected_data = {}
        for key, value in self._objs.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(saved_data, expected_data)


if __name__ == "__main__":
    unittest.main()