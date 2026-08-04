from pydantic import BaseModel, ConfigDict
from datetime import time

class MeetingSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    section_id: int
    begin_time: time | None
    end_time: time | None
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    building: str | None
    room: str | None
    meeting_type: str | None
 