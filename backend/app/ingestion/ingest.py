from app.scraper.client import BannerClient
from app.scraper.parser import parse_section
from app.database import get_db
from app.models.section import Section
from app.models.course import Course
from sqlalchemy import select
from sqlalchemy.orm import Session

def ingest_subject(db: Session, subject: str, term_code: str):
    client = BannerClient()
    client.start_session()
    client.select_term(term_code)
    response = client.search_subject(subject, term_code)

    for section in response["data"]:
        stmt = db.execute(select(Section).where(Section.crn == section["courseReferenceNumber"])).scalar_one_or_none()
        if stmt:
            continue

        course = db.execute(select(Course).where(Course.subjectCourse == section["subjectCourse"])).scalar_one_or_none()
        if not course:
            course_data = {
                "subject": section["subject"],
                "courseNumber": section["courseNumber"],
                "courseTitle": section["courseTitle"],
                "subjectCourse": section["subjectCourse"]
            }
            course = Course(**course_data)
            db.add(course)
            db.flush()
        parsed_section = parse_section(section)
        parsed_section.course_id = course.id
        db.add(parsed_section)

    db.commit()
    

    
        