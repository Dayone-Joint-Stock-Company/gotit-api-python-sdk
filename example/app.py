from flask import Flask
from routes import app_routes
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(app_routes)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG)
