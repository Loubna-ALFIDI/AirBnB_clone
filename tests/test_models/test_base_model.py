#!/usr/bin/python3
'''TestBaseModel'''


from contextlib import AbstractContextManager
from typing import Any
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test module for BaseModel"""
    def test_id(self):
        """test id"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), 36)
        