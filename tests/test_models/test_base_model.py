#!/usr/bin/python3
'''TestBaseModel'''


from contextlib import AbstractContextManager
import os
import json
import datetime
from typing import Any
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test module for BaseModel"""
    def setUp(self):
        """setup the cases to test"""
        self.mymodel = BaseModel()
        self.mymodel.name = "My_First_Model"
        self.mymodel.my_number = 89
        self.id = self.mymodel.id
        self.type_1 = datetime.datetime
        self.my_model_json = self.mymodel.to_dict()

    def test_instance_creation(self):
        """test instance creation"""
        self.assertIsInstance(self.mymodel, BaseModel)

    def test_id(self):
        """test id"""
        self.assertEqual(self.id, self.mymodel.id)
    
    def test_unique_id(self):
        """test unique id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.id, str)
        self.assertEqual(len(base1.id), 36)
        self.assertNotEqual(base1.id, base2.id)

    def test_str(self):
        """test str"""
        self.assertEqual(str(self.mymodel), "[BaseModel] ({}) {}".format(
            self.mymodel.id, self.mymodel.__dict__))

    def test_todict(self):
        """test todict"""
        self.assertEqual(self.mymodel.to_dict(), self.my_model_json)
    
    def test_save(self):
        """test save"""
        self.mymodel.save()
        self.assertNotEqual(self.mymodel.created_at, self.mymodel.updated_at)
    
    def test_created_at(self):
        """test created_at"""
        self.assertIsInstance(self.mymodel.created_at, self.type_1)
    
    def test_updated_at(self):
        """test updated_at"""
        self.assertIsInstance(self.mymodel.updated_at, self.type_1)

    def tearDown(self):
        """teardown the cases to test"""
        pass

if __name__ == '__main__':
    unittest.main()
