from app.scraper.parser import parse_section

sect = {
      "id": 979282,
      "term": "202640",
      "termDesc": "Fall 2026",
      "courseReferenceNumber": "30950",
      "partOfTerm": "1",
      "courseNumber": "010C",
      "courseDisplay": "010C",
      "subject": "CS",
      "subjectDescription": "Computer Science",
      "sequenceNumber": "001",
      "campusDescription": "Riverside",
      "scheduleTypeDescription": "Lecture",
      "courseTitle": "INTRODUCTION TO DATA STRUCTURES AND ALGORITHMS",
      "creditHours": 4,
      "maximumEnrollment": 100,
      "enrollment": 68,
      "seatsAvailable": 32,
      "waitCapacity": 0,
      "waitCount": 0,
      "waitAvailable": 0,
      "crossList": None,
      "crossListCapacity": None,
      "crossListCount": None,
      "crossListAvailable": None,
      "creditHourHigh": 4,
      "creditHourLow": 0,
      "creditHourIndicator": "OR",
      "openSection": True,
      "linkIdentifier": "L1",
      "isSectionLinked": True,
      "subjectCourse": "CS010C",
      "faculty": 
      [
        {
          "bannerId": "8413",
          "category": None,
          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",
          "courseReferenceNumber": "30950",
          "displayName": "Wolf, Kimberley",
          "emailAddress": "kimberley.wolf@ucr.edu",
          "primaryIndicator": False,
          "term": "202640"
        },
        {
          "bannerId": "8414",
          "category": None,
          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",
          "courseReferenceNumber": "30950",
          "displayName": "Montano, Westin",
          "emailAddress": "westin.montano@email.ucr.edu",
          "primaryIndicator": True,
          "term": "202640"
        },
        {
          "bannerId": "8415",
          "category": None,
          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",
          "courseReferenceNumber": "30950",
          "displayName": "Meem, Jannat Ara",
          "emailAddress": "jannatara.meem@email.ucr.edu",
          "primaryIndicator": False,
          "term": "202640"
        },
        {
          "bannerId": "8416",
          "category": None,
          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",
          "courseReferenceNumber": "30950",
          "displayName": "Li, Zhixu",
          "emailAddress": "zhixu.li1@email.ucr.edu",
          "primaryIndicator": False,
          "term": "202640"
        }
      ],
      "meetingsFaculty": 
      [
        {
          "category": "01",
          "class": "net.hedtech.banner.student.schedule.SectionSessionDecorator",
          "courseReferenceNumber": "30950",
          "faculty": 
          [
          ],
          "meetingTime": {
            "beginTime": "1230",
            "building": "CHUNG",
            "buildingDescription": "Winston Chung Hall",
            "campus": "C",
            "campusDescription": "Riverside",
            "category": "01",
            "class": "net.hedtech.banner.general.overall.MeetingTimeDecorator",
            "courseReferenceNumber": "30950",
            "creditHourSession": 4.0,
            "endDate": "12/04/2026",
            "endTime": "1350",
            "friday": False,
            "hoursWeek": 2.66,
            "meetingScheduleType": "LEC",
            "meetingType": "LEC",
            "meetingTypeDescription": "Lecture",
            "monday": False,
            "room": "138",
            "saturday": False,
            "startDate": "09/24/2026",
            "sunday": False,
            "term": "202640",
            "thursday": True,
            "tuesday": True,
            "wednesday": False
          },
          "term": "202640"
        }
      ],
      "reservedSeatSummary": None,
      "sectionAttributes": None,
      "instructionalMethod": "I",
      "instructionalMethodDescription": "In-Person"
    }

result = parse_section(sect)
print(result.crn, result.instructor, result.meetings[0].begin_time)

online_sect = {
      "id": 980459,
      "term": "202640",
      "termDesc": "Fall 2026",
      "courseReferenceNumber": "33958",
      "partOfTerm": "1",
      "courseNumber": "005",
      "courseDisplay": "005",
      "subject": "CS",
      "subjectDescription": "Computer Science",
      "sequenceNumber": "021",
      "campusDescription": "UCR Online",
      "scheduleTypeDescription": "Laboratory",
      "courseTitle": "INTRODUCTION TO COMPUTER PROGRAMMING",
      "creditHours": 0,
      "maximumEnrollment": 105,
      "enrollment": 102,
      "seatsAvailable": 3,
      "waitCapacity": 0,
      "waitCount": 0,
      "waitAvailable": 0,
      "crossList": None,
      "crossListCapacity": None,
      "crossListCount": None,
      "crossListAvailable": None,
      "creditHourHigh": 4,
      "creditHourLow": 0,
      "creditHourIndicator": "OR",
      "openSection": True,
      "linkIdentifier": "B1",
      "isSectionLinked": True,
      "subjectCourse": "CS005",
      "faculty": 
      [
        {
          "bannerId": "8626",
          "category": None,
          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",
          "courseReferenceNumber": "33958",
          "displayName": "Vedadi Gargary, Ashkan",
          "emailAddress": "ashkan.vedadigargary@email.ucr.edu",
          "primaryIndicator": True,
          "term": "202640"
        }
      ],
      "meetingsFaculty": 
      [
        {
          "category": "01",
          "class": "net.hedtech.banner.student.schedule.SectionSessionDecorator",
          "courseReferenceNumber": "33958",
          "faculty": 
          [
          ],
          "meetingTime": {
            "beginTime": None,
            "building": "ONLINE",
            "buildingDescription": "Online",
            "campus": "C",
            "campusDescription": "Riverside",
            "category": "01",
            "class": "net.hedtech.banner.general.overall.MeetingTimeDecorator",
            "courseReferenceNumber": "33958",
            "creditHourSession": 0.0,
            "endDate": "12/04/2026",
            "endTime": None,
            "friday": False,
            "hoursWeek": 2.0,
            "meetingScheduleType": "LAB",
            "meetingType": "LAB",
            "meetingTypeDescription": "Laboratory",
            "monday": False,
            "room": "ONLINE",
            "saturday": False,
            "startDate": "09/24/2026",
            "sunday": False,
            "term": "202640",
            "thursday": False,
            "tuesday": False,
            "wednesday": False
          },
          "term": "202640"
        }
      ],
      "reservedSeatSummary": None,
      "sectionAttributes": None,
      "instructionalMethod": "O",
      "instructionalMethodDescription": "Online"
    }
result2 = parse_section(online_sect)
print(result2.crn, result2.instructor, result2.meetings[0].begin_time)