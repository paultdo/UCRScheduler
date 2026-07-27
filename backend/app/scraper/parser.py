from datetime import time

from app.models.section import Section
from app.models.meeting import Meeting

def parse_time(time_string: str):
    if not time_string:
        return None
    hour = int(time_string[0:2])
    minute = int(time_string[2:])
    return time(hour, minute)

def parse_section(section_data: dict) -> Section:
    crn = section_data["courseReferenceNumber"]
    term_code = section_data["term"]
    sequenceNumber = section_data["sequenceNumber"]
    scheduleTypeDescription = section_data["scheduleTypeDescription"]
    link_type = section_data["linkIdentifier"][0]
    link_group = section_data["linkIdentifier"][1:]
    maximumEnrollment = section_data["maximumEnrollment"]
    seatsAvailable = section_data["seatsAvailable"]
    instructor = None
    enrollment = section_data["enrollment"]
    for i in section_data["faculty"]:
        if i["primaryIndicator"] == True:
            instructor = i["displayName"]
            break
    
    meetings = []
    for meeting in section_data["meetingsFaculty"]:
        meet = meeting["meetingTime"]
        newMeeting = Meeting(
            begin_time = parse_time(meet["beginTime"]),
            end_time = parse_time(meet["endTime"]),
            monday = meet["monday"],
            tuesday = meet["tuesday"],
            wednesday = meet["wednesday"],
            thursday = meet["thursday"],
            friday = meet["friday"],
            saturday = meet["saturday"],
            sunday = meet["sunday"],
            building = meet["building"],
            room = meet["room"],
            meeting_type = meet["meetingType"]
        )
        meetings.append(newMeeting)



    section = Section(
        crn = crn,
        term_code = term_code,
        sequenceNumber = sequenceNumber,
        scheduleTypeDescription = scheduleTypeDescription,
        link_type = link_type,
        link_group = link_group,
        maximumEnrollment = maximumEnrollment,
        seatsAvailable = seatsAvailable,
        instructor = instructor,
        enrollment = enrollment,
        meetings = meetings
    )

    return section

