#!/usr/bin/python3
'''test of the review'''

from models.review import Review
import unittest

class test_Review(unittest.TestCase):
    """ Test review """

    def test_type_text(self):
        """ Verify if thats is instance"""
        self.assertIsInstance(Review.text, str)

    def test_instance_in_object(self):
        """test is instance in the objects"""
        
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(Review.place_id, "")

if __name__ == "__main__":
    unittest.main()
