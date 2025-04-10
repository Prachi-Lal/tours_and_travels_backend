from fastapi import FastAPI
from .routes import tours

app = FastAPI(title="Tours and Travels Backend",
    summary="A backend demonstration for a Tours and Travels Company",
    )

app.include_router(tours.router)
