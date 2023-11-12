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
        self.assertIsInstance(storage.all(), dict)

    def test_new_methode(self):
        """test new methode"""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all().keys())
