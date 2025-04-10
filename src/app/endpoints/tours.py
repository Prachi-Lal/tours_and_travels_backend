from fastapi import Depends
from src.app.database.mongo import get_database
from src.models.tours import tours
from pymongo import *


def fetch_collections(db = get_database()):
    result = []
    db_collection = db.get_collection("users")
    documents = db_collection.find()
    for document in documents:
        document['id'] = str(document['_id']) 
        document.pop('_id')
        result.append(document)
    return result

def search_tours(filters: tours, db = get_database()):
    query = {}
    if filters.countries:
        query["countries"] = {"$in" : filters.countries}
    if filters.cities:
        query["cities"] = {"$in": filters.cities}
    if filters.no_of_days is not None:
        query["no_of_days"] = filters.no_of_days
    if filters.keywords:
        query["keywords"] = {"$in": filters.keywords}
    collection = db.get_collection("users") 
    results = collection.find(query)
    tours = []
    for document in results:
        document["id"] = str(document["_id"])
        document.pop("_id")
        tours.append(document)
    return tours
