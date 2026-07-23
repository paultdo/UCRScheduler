# crn (unique), sequenceNumber, scheduleTypeDescription, link_type, link_group, maximumEnrollment, enrollment, seatsAvailable, instructor fields, FK to Course
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base

class Section(Base):
    __tablename__ = "sections"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    crn: Mapped[str] = mapped_column(String(10), unique=True)
    sequenceNumber: Mapped[str] = mapped_column(String(10))
    scheduleTypeDescription: Mapped[str] = mapped_column(String(500))
    link_type: Mapped[str] = mapped_column(String(50))
    link_group: Mapped[str] = mapped_column(String(50))
    maximumEnrollment: Mapped[int] = mapped_column()
    enrollment: Mapped[int] = mapped_column()
    seatsAvailable: Mapped[int] = mapped_column()
    instructor: Mapped[Optional[str]] = mapped_column(String(200))
    term_code: Mapped[str] = mapped_column(String(10))

    course: Mapped["Course"] = relationship(back_populates="sections")
    meetings: Mapped[List["Meeting"]] = relationship(back_populates="section")
