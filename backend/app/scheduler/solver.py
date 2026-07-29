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



def find_schedules(course_bundles: list[list[tuple]], index, current, results):
    if index >= len(course_bundles):
        results.append(current.copy())
        return

    for bundle in course_bundles[index]:
        conflict = False
        for correct_bundle in current:
            if conflict:
                break
            if bundles_conflict(bundle, correct_bundle):
                conflict = True
                continue

        if conflict:
            continue


        current.append(bundle)
        find_schedules(course_bundles, index + 1, current, results)
        current.pop()