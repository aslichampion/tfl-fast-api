from typing import Optional
from fastapi import FastAPI

from src.api.v1.endpoints import station_departures

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[int] = None):
    return {"item_id": item_id, "q": q}


app.include_router(station_departures.router)
