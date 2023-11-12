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
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.id, str)
        self.assertEqual(len(base1.id), 36)
        self.assertEqual(self.id, self.mymodel.id)

if __name__ == '__main__':
    unittest.main()
