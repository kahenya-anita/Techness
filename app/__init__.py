from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config, config_options
import urllib.request,json
from .models import quote, db


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
Quote = quote.Quote

photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    
    db.init_app(app)
    app.config.from_object(config_options[config_name]) 
    app.config['SECRET_KEY'] = '0806436c2c6ce7'
    app.api_key = api_key['QUOTE_API_KEY']
 
    base_url = app.config["QUOTE_API_BASE_URL"]
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors
    from app.models import User, Post  
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


