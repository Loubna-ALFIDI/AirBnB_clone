#!usr/bin/python3
'''Test City model'''

import unittest
from models.city import City, DataValidationError


class TestCity(unittest.TestCase):
    '''Test City model'''
    def test_create_city(self):
        '''Test creating a new City instance'''
        city = City()
        self.assertIsInstance(city, City)
        # Add more assertions here to test the City instance

    def test_city_attributes(self):
        '''Test the attributes of the City instance'''
        city = City()
        # Set the attributes of the City instance
        city.state_id = "state_id"
        city.name = "name"
        # Add assertions here to test the attributes of the City instance

    def test_city_methods(self):
        '''Test the methods of the City instance'''
        city = City()
        # Call the methods of the City instance and add assertions to test their behavior

    def test_data_validation_error(self):
        '''Test raising a DataValidationError'''
        with self.assertRaises(DataValidationError):
            # Code that raises a DataValidationError
            pass

if __name__ == '__main__':
    unittest.main()