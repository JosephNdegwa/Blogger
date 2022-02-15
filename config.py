import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kariuki_ndegwa:515021@localhost/blogger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False