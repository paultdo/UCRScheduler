def split_subject_course(course_name: str) -> tuple[str, str]:
    index = 0
    while not course_name[index].isdigit():
        index += 1

    subject = course_name[:index]
    number = course_name[index:]

    return (subject, number)