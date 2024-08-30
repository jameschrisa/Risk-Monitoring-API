# app.py
from flask import Flask
from api.routes import api_bp
from utils.caching import cache
from ml.model import init_model

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    cache.init_app(app)
    
    app.register_blueprint(api_bp)
    
    with app.app_context():
        init_model()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])




