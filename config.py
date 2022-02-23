from distutils.command.config import config
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can\'t get it'
    #SECRET_KEY = os.urandom(32)
    #config['SECRET_KEY'] = SECRET_KEY
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kariuki_ndegwa:515021@localhost/blogger'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False