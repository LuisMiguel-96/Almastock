import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-local')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///stockpy.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
