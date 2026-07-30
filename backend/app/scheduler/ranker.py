from datetime import time
from collections import defaultdict

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

def parse_time_to_min(t: time):
    return (t.hour * 60 + t.minute)

def schedule_total_gap_hours(schedule: list[tuple]) -> float:
    days = defaultdict(list)
    total = 0
    for bundle in schedule:
            for section in bundle:
                for meeting in section.meetings:
                    if meeting.begin_time and meeting.end_time:
                        if meeting.monday:
                            days["monday"].append(meeting)
                        if meeting.tuesday:
                            days["tuesday"].append(meeting)
                        if meeting.wednesday:
                            days["wednesday"].append(meeting)
                        if meeting.thursday:
                            days["thursday"].append(meeting)
                        if meeting.friday:
                            days["friday"].append(meeting)
                        if meeting.saturday:
                            days["saturday"].append(meeting)
                        if meeting.sunday:
                            days["sunday"].append(meeting)

    for day in days:
        days[day].sort(key=lambda x: x.begin_time)
        for i in range(len(days[day])):
            if i < len(days[day]) - 1:
                meeting = days[day][i]
                next_meeting = days[day][i + 1]

                gap = parse_time_to_min(next_meeting.begin_time) - parse_time_to_min(meeting.end_time)
                total += gap

    return total / 60


    

    


def schedule_days_used(schedule: list[tuple]) -> int:
    days = set()
    for bundle in schedule:
        for section in bundle:
            for meeting in section.meetings:
                if meeting.monday:
                    days.add("monday")
                if meeting.tuesday:
                    days.add("tuesday")
                if meeting.wednesday:
                    days.add("wednesday")
                if meeting.thursday:
                    days.add("thursday")
                if meeting.friday:
                    days.add("friday")
                if meeting.saturday:
                    days.add("saturday")
                if meeting.sunday:
                    days.add("sunday")

    return len(days)