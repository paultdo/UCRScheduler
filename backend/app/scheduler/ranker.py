from datetime import time

#helper functions
def schedule_latest_end_time(schedule: list[tuple]) -> time:
    if not schedule:
        return None
    latest = None
    for bundle in schedule:
        for section in bundle:
            for meeting in section.meetings:
                if not meeting.end_time:
                    continue
                if latest is None or meeting.end_time > latest:
                    latest = meeting.end_time

    return latest


def schedule_earliest_start_time(schedule: list[tuple]) -> time:
    if not schedule:
            return None
    earliest = None
    for bundle in schedule:
        for section in bundle:
            for meeting in section.meetings:
                if not meeting.begin_time:
                    continue
                if earliest is None or meeting.begin_time < earliest:
                    earliest = meeting.begin_time

    return earliest

def schedule_total_gap_hours(schedule: list[tuple]) -> float:
    pass

def schedule_days_used(schedule: list[tuple]) -> int:
    pass