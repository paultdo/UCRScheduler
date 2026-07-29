from app.scheduler.conflicts import meetings_conflict
from app.models.section import Section
from app.models.meeting import Meeting

def bundles_conflict(bundle_a: tuple[Section, ...], bundle_b: tuple[Section, ...]):
    for section_a in bundle_a:
        for section_b in bundle_b:
            for meeting_a in section_a.meetings:
                for meeting_b in section_b.meetings:
                    if meetings_conflict(meeting_a, meeting_b):
                        return True

    return False



