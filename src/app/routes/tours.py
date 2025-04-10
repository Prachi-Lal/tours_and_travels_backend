from fastapi import APIRouter
from src.app.endpoints.tours import fetch_collections, search_tours
from src.models.tours import tours
from fastapi import Depends
from fastapi import Body
from src.app.database.mongo import get_database
from pymongo.database import Database

router = APIRouter()

@router.get("/")
def root():
    try:
        return fetch_collections()
    except Exception as e:
        return {"Error":str(e)}
    
@router.post("/filtered_tours")
def filter_tours(filters: tours = Body(...),
                 db: Database = Depends(get_database)):
    try:
        return search_tours(filters, db)
    except Exception as e:
        return {"Error":str(e)}