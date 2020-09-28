from flask import Blueprint

def create_app(config_class=Config):
    app = Flask(__name__)

bp = Blueprint('api', __name__)

from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

from app.api import users, errors, tokens
