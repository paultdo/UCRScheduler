# begin_time/end_time (as Time), 7 day booleans, building, room, meetingType, FK to Section
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Time
from datetime import time

from app.database import Base

class Meeting(Base):

    __tablename__ = "meetings"

    id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"))
    begin_time: Mapped[Optional[time]] = mapped_column(Time)
    end_time: Mapped[Optional[time]] = mapped_column(Time)
    monday: Mapped[bool] = mapped_column(default=False)
    tuesday: Mapped[bool] = mapped_column(default=False)
    wednesday: Mapped[bool] = mapped_column(default=False)
    thursday: Mapped[bool] = mapped_column(default=False)
    friday: Mapped[bool] = mapped_column(default=False)
    saturday: Mapped[bool] = mapped_column(default=False)
    sunday: Mapped[bool] = mapped_column(default=False)
    building: Mapped[str] = mapped_column(String(200))
    room: Mapped[str] = mapped_column(String(20))

    section: Mapped["Section"] = relationship(back_populates="meetings")