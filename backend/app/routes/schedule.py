from app.schemas.schedule import ScheduleRequestSchema, ScheduleResponseSchema
from app.schemas.section import SectionSchema
from app.database import get_db
from app.ingestion.utils import split_subject_course
from app.ingestion.ingest import ingest_subject
from app.scheduler.solver import find_schedules
from app.scheduler.ranker import rank_schedules
from app.scheduler.bundles import build_bundles
from app.models.course import Course

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter()

@router.post("/schedule", response_model=ScheduleResponseSchema)
def create_schedule(request: ScheduleRequestSchema, db: Session = Depends(get_db)):
    bundles = []
    for course in request.courses:
        courseObj = db.execute(select(Course).where(Course.subjectCourse == course)).scalar_one_or_none()
        if not courseObj:
            subject, code = split_subject_course(course)
            ingest_subject(db, subject=subject, term_code=request.term_code)

        courseObj = db.execute(select(Course).where(Course.subjectCourse == course)).scalar_one_or_none() if not courseObj else courseObj
        if not courseObj:
            raise HTTPException(status_code=404, detail="Course not found!")
            
        bundles.append(build_bundles(courseObj))

    schedules = []
    find_schedules(bundles, 0, [], schedules)
    ranked_schedules = rank_schedules(schedules=schedules, primary=request.primary, secondary=request.secondary)
    ranked_schedules = ranked_schedules[:request.limit]

    converted_schedules = [
        [
            [SectionSchema.model_validate(section) for section in bundle] for bundle in schedule
        ] for schedule in ranked_schedules
    ]

    response = ScheduleResponseSchema(schedules=converted_schedules)

    return response


        



        