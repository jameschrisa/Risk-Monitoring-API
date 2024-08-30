# ml/model.py
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
from .feature_extraction import extract_features
from .training import train_model

model = None
vectorizer = None

def init_model():
    global model, vectorizer
    try:
        model = joblib.load('phishing_model.joblib')
        vectorizer = joblib.load('vectorizer.joblib')
    except FileNotFoundError:
        print("Model files not found. Training new model...")
        train_model()
        model = joblib.load('phishing_model.joblib')
        vectorizer = joblib.load('vectorizer.joblib')

def analyze_url(url):
    global model, vectorizer
    features = extract_features(url)
    vectorized = vectorizer.transform([url])
    combined_features = np.hstack((vectorized.toarray(), np.array(list(features.values())).reshape(1, -1)))
    prediction = model.predict(combined_features)[0]
    score = model.predict_proba(combined_features)[0][1]
    
    return {
        'url': url,
        'prediction': 'phishing' if prediction == 1 else 'legitimate',
        'phishing_score': float(score),
        'risk_level': 'high' if score > 0.7 else 'medium' if score > 0.4 else 'low',
        'features': features
    }

def analyze_content(content, content_type):
    from .feature_extraction import extract_urls
    urls = extract_urls(content)
    results = [analyze_url(url) for url in urls]
    overall_risk = max([r['phishing_score'] for r in results]) if results else 0
    
    return {
        f'{content_type}_content': content[:50] + '...',
        'urls_analyzed': len(results),
        'overall_risk_level': 'high' if overall_risk > 0.7 else 'medium' if overall_risk > 0.4 else 'low',
        'url_analysis': results
    }

def get_model_patterns():
    global model, vectorizer
    if model is None or vectorizer is None:
        init_model()
    
    feature_names = vectorizer.get_feature_names_out()
    important_features = model.feature_importances_
    
    # Get the top 10 most important features
    top_features = sorted(zip(feature_names, important_features), key=lambda x: x[1], reverse=True)[:10]
    
    patterns = [
        f"Presence of '{feature}' in URL or content (importance: {importance:.2f})"
        for feature, importance in top_features
    ]
    
    return patterns