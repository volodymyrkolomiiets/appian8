import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATION = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_POORT = os.getenv("MYSQL_POORT")

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:{MYSQL_POORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_ECHO = True


class Production(Config):
    pass
