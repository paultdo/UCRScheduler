from app.database import SessionLocal
from app.models.course import Course
from app.scheduler.bundles import build_bundles
from app.scheduler.solver import find_schedules  # adjust path as needed

db = SessionLocal()

# course_names = ["CS061", "CS010B", "MATH010A", "PHYS040A"]
course_names = ["CS011", "WRIT040X", "EE020B", "BIOL002", "HNPG002W"]
courses = [db.query(Course).filter_by(subjectCourse=name).first() for name in course_names]
course_bundles = [build_bundles(c) for c in courses]

results = []
for name, bundles in zip(course_names, course_bundles):
    print(f"{name}: {len(bundles)} bundles")

find_schedules(course_bundles, 0, [], results)

print(f"Total valid schedules found: {len(results)}")
for schedule in results[0:3]:
    for bundle in schedule:
        print([s.crn for s in bundle], end="  ")
    print()
print(f"Total valid schedules found: {len(results)}")

db.close()