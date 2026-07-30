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

def rank_schedules(schedules: list, primary: str = None, secondary: list[str] = None) -> list:
    if not primary and not secondary:
        return schedules

    HEURISTICS = {
        "earliest_end_time": (schedule_latest_end_time, "min_wins"),
        "latest_start_time": (schedule_earliest_start_time, "max_wins"),
        "fewest_gaps": (schedule_total_gap_hours, "min_wins"),
        "fewest_days": (schedule_days_used, "min_wins"),
    }

    # schedules -> schedule -> bundle -> section -> meeting

    def make_sort_key(schedule: list, primary_name: str, secondaries: list):
        primary_func, primary_direction = HEURISTICS[primary_name]
        raw_value = primary_func(schedule)
        value = parse_time_to_min(raw_value) if type(raw_value) == time else raw_value
        if primary_direction == "max_wins":
            value *= -1
        key = (value,)
        for secondary in secondaries:
            raw_secondary_value = HEURISTICS[secondary][0](schedule)
            secondary_value = parse_time_to_min(raw_secondary_value) if type(raw_secondary_value) == time else raw_secondary_value
            if HEURISTICS[secondary][1] == "max_wins":
                secondary_value *= -1
            key += (secondary_value,)

        return key
    new_schedules = []
    for schedule in schedules:
        pair = (make_sort_key(schedule, primary, secondary), schedule)
        new_schedules.append(pair)

    new_schedules.sort(key=lambda pair: pair[0])

    for i in range(len(new_schedules)):
        new_schedules[i] = new_schedules[i][1]

    return new_schedules

    

