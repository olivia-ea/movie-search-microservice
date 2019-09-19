import unittest
from views import app
import json

class TestMovieMicroservice(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_valid_movies_endpoint(self):
        result = self.app.get('/movies/jurassic+park')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn('127 min', data['run_time'])

    def test_invalid_movies_endpoint(self):
        result = self.app.get('/movies/jurassicpark')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 500)
        self.assertIn('Movie not found!', data['Error'])

if __name__ == '__main__':
    unittest.main()