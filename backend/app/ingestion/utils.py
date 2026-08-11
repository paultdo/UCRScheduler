def split_subject_course(course_name: str) -> tuple[str, str]:
    index = 0
    while index < len(course_name) and not course_name[index].isdigit():
        index += 1

    if index >= len(course_name):
        raise ValueError(f"'{course_name}' doesn't look like a valid course code!")

    subject = course_name[:index]
    number = course_name[index:]

    return (subject, number)