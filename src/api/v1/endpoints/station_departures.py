from fastapi import APIRouter, Depends

from src.services.tracker_net import Line, TrackerNetService

router = APIRouter()


@router.get("/stations/{line_code}/{station_code}")
async def station_departures(
    line_code: Line, station_code: str, service: TrackerNetService = Depends()
):
    if line_code not in Line:
        return "oops"
    return await service.station_departures(
        line_code=line_code, station_code=station_code
    )
