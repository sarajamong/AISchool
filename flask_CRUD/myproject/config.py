import os

BASE_DIR=os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR,'myprojectapp.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_ECHO=True

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev') 