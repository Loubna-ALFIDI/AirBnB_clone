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

    def test_instance_creation(self):
        """test instance creation"""
        self.assertIsInstance(self.mymodel, BaseModel)

    def test_id(self):
        """test id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.id, str)
        self.assertEqual(len(base1.id), 36)

if __name__ == '__main__':
    unittest.main()
