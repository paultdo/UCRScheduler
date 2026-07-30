from app.database import SessionLocal
from app.models.section import Section
from app.scheduler.ranker import schedule_latest_end_time  # adjust path
from app.scheduler.ranker import schedule_earliest_start_time
from app.scheduler.ranker import schedule_days_used

db = SessionLocal()

crns = ["13048", "32714", "30948", "32710", "23412", "24080", "17991", "28062", "18012"]
sections = {crn: db.query(Section).filter_by(crn=crn).first() for crn in crns}

# reconstruct the schedule shape: list of bundles (tuples of sections)
test_schedule = [
    (sections["13048"], sections["32714"]),
    (sections["30948"], sections["32710"]),
    (sections["23412"], sections["24080"]),
    (sections["17991"], sections["28062"], sections["18012"]),
]

result = schedule_latest_end_time(test_schedule)
print(result)

result = schedule_earliest_start_time(test_schedule)
print(result)

result = schedule_days_used(test_schedule)
print(result)

db.close()



