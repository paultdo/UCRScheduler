const REFERENCE_MONDAY = new Date("2026-01-05")
const dayOffsets = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

const addDays = (date, days) => {
  const result = new Date(date);
  result.setUTCDate(result.getUTCDate() + days);
  return result;
};

export function meetingToEvents(meeting, sectionLabel) {
    if (!meeting.begin_time || !meeting.end_time) {
        return []
    }
    let list = []

    for (const day in dayOffsets) {

        if(meeting[day]) {
            const placeholderDate = addDays(REFERENCE_MONDAY, dayOffsets[day])
            const dateStr = placeholderDate.toISOString().split('T')[0]
            const start = `${dateStr}T${meeting.begin_time}`
            const end = `${dateStr}T${meeting.end_time}`

            const obj = {
                id: `${meeting.id}-${day}`,
                text: sectionLabel,
                start: start,
                end: end
            }
            list.push(obj)
        }
    }

    return list

}