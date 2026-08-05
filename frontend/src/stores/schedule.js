import { defineStore } from 'pinia'

export const useSchedulesStore = defineStore('schedules', () => {
    const courses = ref([])
    const termCode = ref("")
    const primary = ref("")
    const secondary = ref([])
    const schedules = ref([])
    const currentIndex = ref(0)
    const loading = ref(false)
    const error = ref(false)

    
})