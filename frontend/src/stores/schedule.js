import { defineStore } from 'pinia'
import axios from "axios"
import { ref } from 'vue'

export const useSchedulesStore = defineStore('schedules', () => {
    const courses = ref([])
    const termCode = ref("202640")
    const primary = ref("")
    const secondary = ref([])
    const schedules = ref([])
    const currentIndex = ref(0)
    const loading = ref(false)
    const error = ref(null)
    const limit = ref(20)

    async function fetchSchedules() {
        // separate url logic later
        loading.value = true
        error.value = null
        try {
            const response = await axios.post("http://127.0.0.1:8000/schedule", {
                courses: courses.value,
                term_code: termCode.value,
                primary: primary.value,
                secondary: secondary.value,
                limit: limit.value
            })
            schedules.value = response.data["schedules"]
            currentIndex.value = 0
        } catch(e) {
            error.value = e.message
        } finally {
            loading.value = false
        }
        
    }

    return {
        courses,
        termCode,
        primary,
        secondary,
        schedules,
        currentIndex,
        loading,
        error,
        limit,
        fetchSchedules
    }
})


