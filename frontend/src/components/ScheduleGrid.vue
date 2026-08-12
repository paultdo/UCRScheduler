<script setup>
import { meetingToEvents } from '../utils/calendarTransform'
import { ref, defineProps, computed, watch, onMounted } from 'vue'
import { DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
import { REFERENCE_MONDAY } from '../utils/calendarTransform'

const props = defineProps(['schedule'])
const calendarRef = ref(null)

function scheduleToEvents(schedule) {
    const events = []
    for (const bundle of schedule) {
        for (const section of bundle) {
            for (const meeting of section.meetings) {
                const location = meeting.building ? `${meeting.building} ${meeting.room}` : 'Online/Arranged'
                const sectionLabel = `${section.course_code} ${section.scheduleTypeDescription} (${section.crn}) - ${location}`
                events.push(...meetingToEvents(meeting, sectionLabel))
            }
        }
    }
    return events
}

const calendarEvents = computed(() => scheduleToEvents(props.schedule))

function pushEventsToCalendar() {
    if (calendarRef.value) {
        calendarRef.value.control.update({ events: calendarEvents.value })
    }
}

onMounted(() => {
    pushEventsToCalendar()
})

watch(calendarEvents, () => {
    pushEventsToCalendar()
})
</script>

<template>
    <div class="border rounded overflow-hidden">
        <DayPilotCalendar ref="calendarRef" :cellHeight="40" viewType="Week" :startDate="REFERENCE_MONDAY.toISOString().split('T')[0]" :events="calendarEvents" headerDateFormat="dddd" eventMoveHandling="Disabled" eventResizeHandling="Disabled"/>
    </div>
</template>