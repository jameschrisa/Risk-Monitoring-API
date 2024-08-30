# ml/training.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import joblib
from utils.data_fetcher import fetch_phishtank_data, fetch_alexa_top_sites
from .feature_extraction import extract_features

def train_model():
    print("Fetching training data...")
    phishing_data = fetch_phishtank_data()
    legitimate_data = fetch_alexa_top_sites()
    all_data = phishing_data + legitimate_data
    
    print(f"Training on {len(all_data)} URLs ({len(phishing_data)} phishing, {len(legitimate_data)} legitimate)")
    
    X = [item[0] for item in all_data]
    y = [1 if item[1] == 'phishing' else 0 for item in all_data]
    
    feature_dicts = [extract_features(url) for url in X]
    
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    
    X_combined = np.hstack((X_vectorized.toarray(), np.array(list(map(lambda x: list(x.values()), feature_dicts)))))
    
    X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy}")

    joblib.dump(model, 'phishing_model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')



# utils/__init__.py
# This file can be left empty
