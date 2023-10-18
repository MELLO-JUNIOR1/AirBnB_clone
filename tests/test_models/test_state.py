#!/usr/bin/python3
'''test of the state'''

import unittest
import sys
import models
from models.state import State


class test_State( unittest.TestCase ):
    """ Test of the state"""

    def test_type_name( self) :
        """test of the type"""
        self.assertIsInstance( State.name, str )

    def test_instance_in_object(self):
        """test is instance in the objects"""
        self.assertTrue( hasattr(State, "name") )
        self.assertEqual( State.name, "" )

if __name__ == "__main__":
    unittest.main()
