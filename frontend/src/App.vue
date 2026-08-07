<script setup>
import CourseInput from './components/CourseInput.vue';
import ScheduleBrowser from './components/ScheduleBrowser.vue';
import { meetingToEvents } from './utils/calendarTransform.js'

const fakeMeeting = {
    id: 1,
    begin_time: "09:30:00",
    end_time: "10:50:00",
    monday: true,
    tuesday: false,
    wednesday: true,
    thursday: false,
    friday: false,
    saturday: false,
    sunday: false
}

console.log(meetingToEvents(fakeMeeting, "CS010A Lecture (30921)"))


</script>

<template>
  <CourseInput />
  <ScheduleBrowser />
</template>
