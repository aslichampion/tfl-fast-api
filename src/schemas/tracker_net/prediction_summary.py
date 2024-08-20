from datetime import datetime, timedelta
from typing import List

from pydantic import field_validator
from pydantic_xml import BaseXmlModel, attr, element


class Train(BaseXmlModel):
    set_number: str = attr(name="S")
    trip_number: str = attr(name="T")
    destination_code: str = attr(name="D")
    countdown_time: timedelta = attr(name="C")
    location_status: str = attr(name="L")
    destination_name: str = attr(name="DE")
    arrival_time: str = attr(name="AT")
    departure_time: str = attr(name="DT")

    @field_validator("countdown_time", mode="before")
    def parse_timedelta(cls, value: str) -> timedelta:
        if value == "-":
            return timedelta(seconds=0)
        else:
            minutes, seconds = map(int, value.split(":"))
            return timedelta(minutes=minutes, seconds=seconds)


class Platform(BaseXmlModel):
    name: str = attr(name="N")
    code: str = attr(name="Code")
    next: str = attr(name="Next")
    trains: List[Train] = element(tag="T", default_factory=list)


class Station(BaseXmlModel):
    code: str = attr(name="Code")
    name: str = attr(name="N")
    platforms: List[Platform] = element(tag="P")


class Time(BaseXmlModel):
    timestamp: datetime = attr(name="TimeStamp")

    @field_validator("timestamp", mode="before")
    def parse_timestamp(cls, value: str) -> datetime:
        return datetime.strptime(value, "%Y/%m/%d %H:%M:%S")


class Root(BaseXmlModel, tag="ROOT"):
    time: Time = element(tag="Time")
    stations: List[Station] = element(tag="S")
