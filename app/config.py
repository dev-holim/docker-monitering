import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY="002bef7afacd4d3c92634783c6e215e1"

class DevelopmentConfig(Config):
    DEBUG = True

class DatabaseConfig:
    NAME = os.environ["DATABASE_NAME"]
    HOST = os.environ["DATABASE_HOST"]
    PORT = os.environ["DATABASE_PORT"]
    USER_NAME = os.environ["DATABASE_USER_NAME"]
    USER_PASSWORD = os.environ["DATABASE_USER_PASSWORD"]
    DATABASE_SCHEMA = os.environ["DATABASE_SCHEMA"]

    URL = f"postgresql+asyncpg://{USER_NAME}:{USER_PASSWORD}@{HOST}:{PORT}/{NAME}?{DATABASE_SCHEMA}"