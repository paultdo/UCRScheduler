from pydantic import BaseModel, ConfigDict
from app.schemas.meeting import MeetingSchema

class SectionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    course_id: int
    crn: str
    sequenceNumber: str
    scheduleTypeDescription: str
    link_type: str | None
    link_group: str | None
    maximumEnrollment: int
    enrollment: int
    seatsAvailable: int
    instructor: str | None
    term_code: str
    meetings: list[MeetingSchema]
    
