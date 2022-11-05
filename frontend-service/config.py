import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__name__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    WTF_CSRF_SECRET_KEY = os.environ["WTF_CSRF_SECRET_KEY"]


class DevelopmentConfig(Config):
    ENV = "develpoment"
    DEBUG = True


class ProductionConfig(Config):
    pass