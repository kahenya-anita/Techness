import os



class Config:
    SECRET_KEY =  os.urandom(32)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://ufettalxnucmjx:bc8adac604a7cdeeecd391b2ae7efaf20f99bf4a6b5aff6a314ea6ac4a3c7f3b@ec2-52-72-34-184.compute-1.amazonaws.com:5432/dau239uqj5r9ot'
    QUOTE_API_BASE_URL = 'GET http://quotes.stormconsultancy.co.uk/quotes.json'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://ufettalxnucmjx:bc8adac604a7cdeeecd391b2ae7efaf20f99bf4a6b5aff6a314ea6ac4a3c7f3b@ec2-52-72-34-184.compute-1.amazonaws.com:5432/dau239uqj5r9ot'   


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}