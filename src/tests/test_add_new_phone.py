import unittest
import requests


class TestAddPhone(unittest.TestCase):

    def test_successful_add(self):
        # Given
        phone_added = {
            "description": "mobile",
            "country_code": "1",
            "phone_no": "3476290991"
        }

        # When
        # Should first add a student with uni=ab1234
        response = requests.post('http://localhost:5013/api/contacts/ab1234/new_phone',
                                 json=phone_added)

        # Then
        self.assertEqual(200, response.status_code)
