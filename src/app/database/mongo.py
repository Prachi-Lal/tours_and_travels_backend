import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path 

env_path =  Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

connection_string = os.getenv("mongodb_url")
database_name = os.getenv("database")

if not connection_string or not database_name:
    raise Exception("Missing MongoDB URL or Database Name in environment variables")

client = MongoClient(connection_string)


def get_database():
    return client[database_name]

