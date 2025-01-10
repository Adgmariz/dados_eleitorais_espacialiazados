from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def criar_conexao():
    load_dotenv()

    DATABASE_USER = os.getenv('DB_USER')
    DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE_HOST = os.getenv('DB_HOST')
    DATABASE_PORT = os.getenv('DB_PORT')
    DATABASE_NAME = os.getenv('DB_NAME')

    return create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')
