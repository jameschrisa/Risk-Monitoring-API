# api/routes.py
from flask import Blueprint, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from ml.model import analyze_url, analyze_content, get_model_patterns
from utils.caching import cache
from utils.data_fetcher import get_recent_phishing_trends

api_bp = Blueprint('api', __name__)
limiter = Limiter(key_func=get_remote_address)

@api_bp.route('/analyze_url', methods=['POST'])
@limiter.limit("10 per minute")
def analyze_url_route():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    result = analyze_url(url)
    return jsonify(result)

@api_bp.route('/analyze_email', methods=['POST'])
@limiter.limit("5 per minute")
def analyze_email_route():
    email_content = request.json.get('email_content')
    if not email_content:
        return jsonify({"error": "No email content provided"}), 400
    
    result = analyze_content(email_content, content_type='email')
    return jsonify(result)

@api_bp.route('/analyze_message', methods=['POST'])
@limiter.limit("5 per minute")
def analyze_message_route():
    message = request.json.get('message')
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    result = analyze_content(message, content_type='message')
    return jsonify(result)

@api_bp.route('/get_patterns', methods=['GET'])
@limiter.limit("100 per minute")
@cache.cached(timeout=3600)  # Cache for 1 hour
def get_patterns():
    model_patterns = get_model_patterns()
    recent_trends = get_recent_phishing_trends()
    
    patterns = {
        'model_based_patterns': model_patterns,
        'recent_phishing_trends': recent_trends
    }
    
    return jsonify(patterns)

# ml/__init__.py
# This file can be left empty