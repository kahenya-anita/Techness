from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config, config_options
from app import app
import urllib.request,json
from .models import quote


Quote = quote.Quote
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    
    db.init_app(app)
    app.config.from_object(config_options[config_name]) 
    app.config['SECRET_KEY'] = '0806436c2c6ce7'
    app.api_key = api key['QUOTES_API_KEY']

    
    # configure UploadSet
    configure_uploads(app,photos)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
