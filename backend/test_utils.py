from app.ingestion.utils import split_subject_course  # adjust path to wherever you put it

test_cases = ["CS010A", "MATH010A", "PHYS040A", "CS005", "CS010C"]
for name in test_cases:
    print(name, "->", split_subject_course(name))