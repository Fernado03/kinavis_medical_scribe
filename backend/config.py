import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'fernado03'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'KHOftPjjsa!I1bS3'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'ai_medical_scribe'
    MYSQL_CURSORCLASS = 'DictCursor' # Optional: To get results as dictionaries

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Ensure sensitive data is loaded from environment variables in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}