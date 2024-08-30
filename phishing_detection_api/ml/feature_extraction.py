# ml/feature_extraction.py
from urllib.parse import urlparse
import re

def extract_features(url):
    parsed_url = urlparse(url)
    
    features = {
        'length': len(url),
        'num_subdomains': len(parsed_url.netloc.split('.')) - 1,
        'has_http': 1 if parsed_url.scheme == 'http' else 0,
        'has_https': 1 if parsed_url.scheme == 'https' else 0,
        'has_ip': 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0,
        'has_at': 1 if '@' in url else 0,
        'has_double_slash': 1 if '//' in parsed_url.path else 0,
        'has_dash': 1 if '-' in parsed_url.netloc else 0,
        'has_suspicious_words': 1 if any(word in url.lower() for word in ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'signin']) else 0
    }
    return features

def extract_urls(content):
    return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
