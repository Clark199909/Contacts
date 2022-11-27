import unittest
import requests


class TestAddAddress(unittest.TestCase):

    def test_successful_add(self):
        # Given
        address_added = {
            "description": "home",
            "country": "USA",
            "state": "NY",
            "city": "NY",
            "zip_code": "10025",
            "street": "125W 109th St"
        }

        # When
        # Should first add a student with uni=ab1234
        response = requests.post('http://localhost:5013/api/contacts/ab1234/new_address',
                                 json=address_added)

        # Then
        self.assertEqual(200, response.status_code)
