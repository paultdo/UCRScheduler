from app.models.section import Section
from app.models.meeting import Meeting
from app.scheduler.ranker import schedule_total_gap_hours
from app.scraper.parser import parse_time

m1 = Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)
m2 = Meeting(begin_time=parse_time("1300"), end_time=parse_time("1400"), monday=True)

section_a = Section(meetings=[m1])
section_b = Section(meetings=[m2])

test_schedule = [(section_a,), (section_b,)]

result = schedule_total_gap_hours(test_schedule)
print(result)  # expected: 120 (2 hour gap, in minutes) — or 2.0 if you convert to hours