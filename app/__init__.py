import os
from flask import Flask
from dotenv import load_dotenv
from config import config_dict

load_dotenv()

def create_app():
    app = Flask(__name__)
    config_type = os.getenv('CONFIG_TYPE',default='development')
    app.config.from_object(config_dict[config_type])

    register_blueprints(app)
    return app

def register_blueprints(app):
    from app.routes import routes
    app.register_blueprint(routes)
