from app.database import SessionLocal
from app.models.course import Course
from app.scheduler.bundles import build_bundles

db = SessionLocal()
course = db.query(Course).filter_by(subjectCourse="CS010A").first()
bundles = build_bundles(course)

print(len(course.sections))

print(f"Total bundles: {len(bundles)}")
for bundle in bundles:
    print([s.crn for s in bundle])

db.close()