from app.database import SessionLocal
from app.models.course import Course
from app.scheduler.bundles import build_bundles

db = SessionLocal()

# from app.models.course import Course
# all_courses = db.query(Course).filter(Course.subjectCourse.like("CS%")).all()
# print([c.subjectCourse for c in all_courses])
course = db.query(Course).filter_by(subjectCourse="CS010C").first()
bundles = build_bundles(course)

print(len(course.sections))

print(f"Total bundles: {len(bundles)}")
for bundle in bundles:
    print([s.crn for s in bundle])

db.close()