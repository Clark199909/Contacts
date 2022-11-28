import unittest
import requests

# clear the database before doing this test


class TestGetAllPhonesOfOneStudent(unittest.TestCase):

    def test_empty_response(self):
        response = requests.get('http://localhost:5013/api/contacts/all_phones')
        self.assertEqual(response.text, '[]\n')
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        # Given

        response = requests.get('http://localhost:5013/api/contacts/all_phones')

        # Then
        print(response.text)
        self.assertEqual(200, response.status_code)