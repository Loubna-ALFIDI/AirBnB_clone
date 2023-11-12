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
    
    def test_count(self):
        """Test count"""
        self.assertTrue(hasattr(storage, "count"))

    def test_all_methode(self):
        """test all methode"""
        result = storage.all()
        self.assertEqual(result, self._objs)
