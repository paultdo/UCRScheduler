from app.models.meeting import Meeting
from app.scheduler.conflicts import meetings_conflict
from app.scraper.parser import parse_time

# begin_time: Mapped[Optional[time]] = mapped_column(Time)
# end_time: Mapped[Optional[time]] = mapped_column(Time)
# monday: Mapped[bool] = mapped_column(default=False)
# tuesday: Mapped[bool] = mapped_column(default=False)
# wednesday: Mapped[bool] = mapped_column(default=False)
# thursday: Mapped[bool] = mapped_column(default=False)
# friday: Mapped[bool] = mapped_column(default=False)
# saturday: Mapped[bool] = mapped_column(default=False)
# sunday: Mapped[bool] = mapped_column(default=False)


meeting_1 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)
meeting_2 = Meeting(begin_time=parse_time("1030"), end_time=parse_time("1130"), monday=True)

meeting_3 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)
meeting_4 = Meeting(begin_time=parse_time("1100"), end_time=parse_time("1130"), monday=True)

meeting_5 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)
meeting_6 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), tuesday=True)

meeting_7 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)
meeting_8 = Meeting(monday=True)

print("Test 1: ", meetings_conflict(meeting_1, meeting_2))
print("Test 2: ", meetings_conflict(meeting_3, meeting_4))
print("Test 3: ", meetings_conflict(meeting_5, meeting_6))
print("Test 4: ", meetings_conflict(meeting_7, meeting_8))