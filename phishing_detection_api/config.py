# config.py
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', 'False') == 'True'
CACHE_TYPE = os.getenv('CACHE_TYPE', "SimpleCache")
CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 300))
RATELIMIT_DEFAULT = os.getenv('RATELIMIT_DEFAULT', "100 per minute")
PHISHTANK_API_URL = os.getenv('PHISHTANK_API_URL', "http://data.phishtank.com/data/")
PHISHTANK_API_KEY = os.getenv('PHISHTANK_API_KEY')
ALEXA_TOP_SITES_URL = os.getenv('ALEXA_TOP_SITES_URL', "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")

if not PHISHTANK_API_KEY:
    raise ValueError("PHISHTANK_API_KEY is not set in the environment variables")
