from app.database import SessionLocal
from app.models.course import Course
from app.scheduler.bundles import build_bundles
from app.scheduler.solver import find_schedules
from app.scheduler.ranker import rank_schedules, schedule_latest_end_time

db = SessionLocal()

course_names = ["CS061", "CS010B", "MATH010A", "PHYS040A"]
courses = [db.query(Course).filter_by(subjectCourse=name).first() for name in course_names]
course_bundles = [build_bundles(c) for c in courses]

results = []
find_schedules(course_bundles, 0, [], results)
print(f"Total valid schedules found: {len(results)}")

ranked = rank_schedules(results, primary="earliest_end_time", secondary=["fewest_gaps"])

print("\nTop 3 ranked schedules:")
for schedule in ranked[:3]:
    for bundle in schedule:
        print([s.crn for s in bundle], end="  ")
    print()

all_end_times = [schedule_latest_end_time(s) for s in results]
print("\nMinimum end time across all schedules:", min(all_end_times))
print("End time of #1 ranked schedule:", schedule_latest_end_time(ranked[0]))

db.close()