from pydantic import BaseModel, ConfigDict
from app.schemas.section import SectionSchema
from typing import Literal

class ScheduleRequestSchema(BaseModel):
    courses: list[str]
    term_code: str
    primary: Literal["earliest_end_time", "latest_start_time"]
    secondary: list[str] = []
    limit: int = 20

class ScheduleResponseSchema(BaseModel):
    schedules: list[list[list[SectionSchema]]]
