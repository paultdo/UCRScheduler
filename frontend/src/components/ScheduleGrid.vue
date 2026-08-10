<script setup>
    import { meetingToEvents } from '../utils/calendarTransform'
    import { ref, defineProps, computed, watch, onMounted } from 'vue'
    import { DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
    import { REFERENCE_MONDAY } from '../utils/calendarTransform'


    const props = defineProps(['schedule'])

    const calendarRef = ref(null)

    function scheduleToEvents(schedule) {
        const events = []
        for(const bundle of schedule) {
            for(const section of bundle) {
                const sectionLabel = `${section.scheduleTypeDescription} (${section.crn})`
                for(const meeting of section.meetings) {
                    events.push(...meetingToEvents(meeting, sectionLabel))
                }
            }
        }

        return events
    }

    const calendarEvents = computed(() => scheduleToEvents(props.schedule))

    function pushEventsToCalendar() {
        if(calendarRef.value) {
            calendarRef.value.control.update({events: calendarEvents.value})
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
    <DayPilotCalendar ref="calendarRef" viewType="Week" :startDate="REFERENCE_MONDAY.toISOString().split('T')[0]" :events="calendarEvents" headerDateFormat="dddd" />
</template>