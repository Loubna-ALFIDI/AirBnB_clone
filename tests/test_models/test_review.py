#!/usr/bin/python3
"""Unittest for review"""
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """Unittest for review"""
    def test_save(self):
        """test save"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)
    
    def test_str(self):
        """test str"""
        review = Review()
        review.save()
        self.assertEqual(str(review), "[Review] ({}) {}".format(review.id, review.__dict__))
    
    def test_type_review(self):
        """test type review"""
        self.new_review = Review()
        self.assertEqual(self.new_review.place_id, "")
        self.assertEqual(self.new_review.user_id, "")
        self.assertEqual(self.new_review.text, "")
    
if __name__ == '__main__':
    unittest.main()
