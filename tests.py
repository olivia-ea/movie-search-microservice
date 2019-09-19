import unittest
from movieutils import app
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
        self.assertIn('1993', data['year_released'])

    def test_invalid_movies_endpoint(self):
        result = self.app.get('/movies/jurassicpark')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 500)
        self.assertIn('Movie not found!', data['Error'])

    def test_valid_movies_search_endpoint(self):
        result = self.app.get('/movies/search/jurassic+park')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn('1993', data['Results'][0]['year_released'])

    def test_invalid_movies_search_endpoint(self):
        result = self.app.get('/movies/jurassicpark')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 500)
        self.assertIn('Movie not found!', data['Error'])

    def test_valid_movies_search_with_year_endpoint(self):
        result = self.app.get('/movies/search/jurassic+park/1993')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn('1993', data['Results'][0]['year_released'])

    def test_invalid_movies_search_with_valid_year_endpoint(self):
        result = self.app.get('/movies/search/jurassicpark/1992')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 500)
        self.assertIn('Movie not found!', data['Error'])

    def test_movies_search_with_invalid_year_endpoint(self):
        result = self.app.get('/movies/search/jurassicpark/0000')
        encoded_data = result.data.decode("utf-8")
        self.assertEqual(result.status_code, 400)
        self.assertEqual("Not a valid year!", encoded_data)

if __name__ == '__main__':
    unittest.main()