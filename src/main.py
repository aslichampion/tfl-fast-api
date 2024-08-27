from fastapi import FastAPI

from src.api.v1.endpoints import station_departures

app = FastAPI()


@app.get("/ping")
def read_root():
    return {"ping": "pong"}

app.include_router(station_departures.router)
