# tests/test_api.py
import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_analyze_url(self):
        response = self.client.post('/analyze_url', json={'url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('prediction', data)
        self.assertIn('phishing_score', data)

    def test_analyze_email(self):
        response = self.client.post('/analyze_email', json={'email_content': 'Test email with http://example.com link'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('overall_risk_level', data)
        self.assertIn('url_analysis', data)

    def test_get_patterns(self):
        response = self.client.get('/get_patterns')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('model_based_patterns', data)
        self.assertIn('recent_phishing_trends', data)