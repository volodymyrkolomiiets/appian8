import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_POORT = os.getenv("MYSQL_POORT")
    HOST = "localhost"

    if os.getenv("DOCKER_HOST"):
        HOST = "order-db"
        MYSQL_POORT = 3306

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{HOST}:{MYSQL_POORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    pass
