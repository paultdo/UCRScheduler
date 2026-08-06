<script setup>
import { useSchedulesStore } from "../stores/schedule"
import { ref } from 'vue'

const store = useSchedulesStore()
const courseCode = ref("")

function addCourse() {
    store.courses.push(courseCode.value.trim())
    courseCode.value = ""
}

function deleteCourse(deletedCourse) {
    store.courses = store.courses.filter(course => course !== deletedCourse)
}
</script>

<template>
    <ul class="list-group">
        <li class="list-group-item" v-for="course in store.courses">
            {{ course }}
            <button class="btn btn-danger" @click="deleteCourse(course)">X</button>
        </li>
    </ul>
    <form @submit.prevent>
        <div class="mb-3">
            <label for="courseCode" class="form-label">Course</label>
            <input type="text" class="form-control" id="courseCode" v-model="courseCode">
        </div>
        <button type="button" class="btn btn-primary" @click="addCourse">Add Course</button>

        <div class="mb-3">
            <label for="termCode" class="form-label">Term Code</label>
            <input type="text" class="form-control" id="termCode" v-model="store.termCode">
        </div>

        <select id="primary" class="form-select" v-model="store.primary">
            <option value="earliest_end_time">Earliest End Time</option>
            <option value="latest_start_time">Latest Start Time</option>
        </select>

        <select v-model="store.secondary" id="secondary" multiple>
            <option value="fewest_gaps">Fewest gaps</option>
            <option value="fewest_days">Fewest days</option>
        </select>

        <button class="btn btn-primary" @click="store.fetchSchedules()">Fetch Courses</button>
    </form>
</template>