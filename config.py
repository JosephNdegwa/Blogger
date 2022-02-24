import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can\'t get it'
    #SECRET_KEY = os.urandom(32)
    #config['SECRET_KEY'] = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kariuki_ndegwa:515021@localhost/blogger'
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False



    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kariuki_ndegwa:515021@localhost/blogger'
    DEBUG = True


config = {
'development':DevConfig,
'production':ProdConfig
}