<script setup>
import { useSchedulesStore } from "../stores/schedule"
import { ref } from 'vue'
import { TERMS } from "../utils/terms"

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
    <div class="card shadow-sm">
        <div class="card-body">
            <h5 class="card-title mb-3">Build Your Schedule</h5>

            <div v-if="store.error" class="alert alert-danger" role="alert">
                {{ store.error }}
            </div>

            <ul class="list-group mb-3" v-if="store.courses.length > 0">
                <li class="list-group-item d-flex justify-content-between align-items-center" v-for="course in store.courses" :key="course">
                    <span>{{ course }}</span>
                    <button class="btn btn-sm btn-danger" @click="deleteCourse(course)">✕</button>
                </li>
            </ul>

            <form @submit.prevent>
                <div class="row g-2 align-items-end mb-3">
                    <div class="col">
                        <label for="courseCode" class="form-label">Course</label>
                        <input type="text" class="form-control" id="courseCode" placeholder="e.g. CS010A" v-model="courseCode">
                    </div>
                    <div class="col-auto">
                        <button type="button" class="btn btn-outline-primary" @click="addCourse">Add Course</button>
                    </div>
                </div>

                <div class="mb-3">
                    <label for="termCode" class="form-label">Term Code</label>
                    <select name="termCode" class="form-select" id="termCode" v-model="store.termCode">
                        <option v-for="term in TERMS" :value="term.code">{{ term.label }}</option>
                    </select>
                </div>

                <div class="mb-3">
                    <label for="primary" class="form-label">Rank by</label>
                    <select id="primary" class="form-select" v-model="store.primary" required>
                        <option value="earliest_end_time">Earliest End Time</option>
                        <option value="latest_start_time">Latest Start Time</option>
                    </select>
                </div>

                <div class="mb-4">
                    <label for="secondary" class="form-label">Also prefer (ctrl/cmd + click for multiple)</label>
                    <select v-model="store.secondary" id="secondary" class="form-select" multiple>
                        <option value="fewest_gaps">Fewest gaps</option>
                        <option value="fewest_days">Fewest days</option>
                    </select>
                </div>

                <button class="btn btn-primary w-100" @click="store.fetchSchedules()" :disabled="store.loading">
                    <span v-if="store.loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                    {{ store.loading ? 'Loading...' : 'Fetch Courses' }}
                </button>
            </form>
        </div>
    </div>
</template>