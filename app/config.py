import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://imhzviysnluuzo:517571e6fc8738ecf51f66dad56828bcbdf6ebb63ddca07a1a4b8c609d83252e@ec2-34-198-31-223.compute-1.amazonaws.com:5432/d1ebs7k7931um3''
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER= os.environ.get('UPLOAD_FOLDER') or 'uploads'
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False