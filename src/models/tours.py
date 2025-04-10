from pydantic import BaseModel 
from typing import Optional, List

class tours(BaseModel):
    id: Optional[str] = None
    countries: Optional[List[str]]  = None
    cities: Optional[List[str]]  = None
    no_of_days: Optional[int]  = None
    keywords: Optional[List[str]]  = None

    