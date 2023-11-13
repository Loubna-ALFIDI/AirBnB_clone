#!/usr/bin/python3
"""Unittest for amenity"""
import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """Unittest for amenity"""
    def test_name(self):
        """Test name"""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")
    
    def test_state_id(self):
        """Test state_id"""
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")
    
    def test_id(self):
        """Test id"""
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        self.assertIsInstance(city.id, str)
        self.assertEqual(len(city.id), 36)
    
    def test_str(self):
        """Test str"""
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        self.assertEqual(str(city), "[City] ({}) {}".format(city.id, city.__dict__))
    
    def test_save(self):
        """Test save"""
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

if __name__ == '__main__':
    unittest.main()
