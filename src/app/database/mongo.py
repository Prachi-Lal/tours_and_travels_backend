import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("mongodb_url")
database_name = os.getenv("database")

client = MongoClient(connection_string)


def get_database():
    return client.get_database(database_name)
