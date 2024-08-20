from enum import Enum
import logging
from src.schemas.tracker_net.prediction_summary import Root, Station
from src.utils import http_client


class Line(Enum):
    BAKERLOO = "B"
    CENTRAL = "C"
    DISTRICT = "D"
    HAMMERSMITH_AND_CIRCLE = "H"
    JUBILEE = "J"
    METROPOLITAN = "M"
    NORTHERN = "N"
    PICCADILLY = "P"
    VICTORIA = "V"
    WATERLOO_AND_CITY = "W"


class TrackerNetService:
    def __init__(self):
        self.client = http_client.httpx_client
        self.summary_base_url = "https://api.tfl.gov.uk/TrackerNet/PredictionSummary"

    async def station_departures(self, line_code: Line, station_code: str):
        url = f"{self.summary_base_url}/{line_code.value}"
        logging.info(url)
        response = await self.client.get(url=url)
        xml_string = response.text
        root = Root.from_xml(xml_string)
        station: Station = next(
            station for station in root.stations if station.code == station_code
        )
        return station
