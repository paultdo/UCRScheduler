from app.models.meeting import Meeting

def meetings_conflict(meeting_a: Meeting, meeting_b: Meeting) -> bool:
    if meeting_a.begin_time == None or meeting_b.begin_time == None:
        return False

    daysA = {
        "monday": False,
        "tuesday": False,
        "wednesday": False,
        "thursday": False,
        "friday": False,
        "saturday": False,
        "sunday": False
    }

    daysB = {
        "monday": False,
        "tuesday": False,
        "wednesday": False,
        "thursday": False,
        "friday": False,
        "saturday": False,
        "sunday": False
    }

    for day in daysA:
        daysA[day] = getattr(meeting_a, day)

    for day in daysB:
            daysB[day] = getattr(meeting_b, day)

    commonDays = set()
    for day in daysA:
         if daysA[day] and daysB[day]:
              commonDays.add(day)

    if not commonDays:
         return False
    
    if meeting_a.begin_time < meeting_b.end_time and meeting_b.begin_time < meeting_a.end_time:
         return True


    return False


    