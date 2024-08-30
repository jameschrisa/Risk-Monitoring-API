# utils/data_fetcher.py
import requests
import zipfile
import io
from bs4 import BeautifulSoup
from config import PHISHTANK_API_URL, ALEXA_TOP_SITES_URL
from utils.caching import cache

@cache.memoize(timeout=86400)  # Cache for 24 hours
def fetch_phishtank_data():
    try:
        response = requests.get(PHISHTANK_API_URL)
        response.raise_for_status()
        data = response.json()
        return [(item['url'], 'phishing') for item in data]
    except requests.RequestException as e:
        print(f"Error fetching PhishTank data: {e}")
        return []

@cache.memoize(timeout=86400)  # Cache for 24 hours
def fetch_alexa_top_sites(num_sites=1000):
    try:
        response = requests.get(ALEXA_TOP_SITES_URL)
        response.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            with zip_ref.open('top-1m.csv') as csv_file:
                return [(line.decode().strip().split(",")[1], 'legitimate') for line in csv_file.readlines()[:num_sites]]
    except requests.RequestException as e:
        print(f"Error fetching Alexa top sites: {e}")
        return []

@cache.memoize(timeout=86400)  # Cache for 24 hours
def get_recent_phishing_trends():
    try:
        # This is a placeholder URL. Replace with a real source of phishing trends.
        response = requests.get("https://www.phishing.org/phishing-alerts")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # This is a placeholder extraction. Adjust based on the actual website structure.
        trends = [item.text.strip() for item in soup.select('.phishing-trend-item')[:5]]
        
        return trends
    except requests.RequestException as e:
        print(f"Error fetching recent phishing trends: {e}")
        return ["Unable to fetch recent trends"]