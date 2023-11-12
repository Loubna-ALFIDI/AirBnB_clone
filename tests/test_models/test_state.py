#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests for State class"""
    def test_name(self):
        """Test name"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
    
    def test_id(self):
        """Test id"""
        state = State()
        state.name = "California"
        self.assertIsInstance(state.id, str)
        self.assertEqual(len(state.id), 36)
    
    def test_str(self):
        """Test str"""
        state = State()
        state.name = "California"
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__))

if __name__ == '__main__':
    unittest.main()
