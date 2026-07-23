# subject, courseNumber, courseTitle, subjectCourse (unique)
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(30))
    courseNumber: Mapped[str] = mapped_column(String(30))
    courseTitle: Mapped[str] = mapped_column(String(500))
    subjectCourse: Mapped[str] = mapped_column(String(30), unique=True)

    sections: Mapped[List["Section"]] = relationship(back_populates="course")

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}, Subject={self.subject!r}, Course Number={self.courseNumber!r}, Course Title = {self.courseTitle!r})"