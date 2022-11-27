import unittest
import requests


class TestAddEmail(unittest.TestCase):

    def test_successful_add(self):
        # Given
        email_added = {
            "description": "personal",
            "address": "dw3013@columbia.edu"
        }

        # When
        # Should first add a student with uni=ab1234
        response = requests.post('http://localhost:5013/api/contacts/ab1234/new_email',
                                 json=email_added)

        # Then
        self.assertEqual(200, response.status_code)
