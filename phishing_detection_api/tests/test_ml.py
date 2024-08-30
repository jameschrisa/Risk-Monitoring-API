# tests/test_ml.py
import unittest
from ml.feature_extraction import extract_features, extract_urls
from ml.model import analyze_url

class TestML(unittest.TestCase):
    def test_extract_features(self):
        url = "http://example.com/path?param=value"
        features = extract_features(url)
        self.assertIsInstance(features, dict)
        self.assertIn('length', features)
        self.assertIn('has_http', features)

    def test_extract_urls(self):
        content = "Visit http://example.com and https://test.com"
        urls = extract_urls(content)
        self.assertEqual(len(urls), 2)
        self.assertIn("http://example.com", urls)
        self.assertIn("https://test.com", urls)

    def test_analyze_url(self):
        url = "http://example.com"
        result = analyze_url(url)
        self.assertIn('prediction', result)
        self.assertIn('phishing_score', result)
        self.assertIn('risk_level', result)

