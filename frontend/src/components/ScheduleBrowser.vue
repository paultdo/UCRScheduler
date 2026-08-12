<script setup>
import { useSchedulesStore } from '../stores/schedule';
import ScheduleGrid from './ScheduleGrid.vue';
const store = useSchedulesStore()

function decrement() {
    if (store.currentIndex > 0) {
        store.currentIndex--
    }
}

function increment() {
    if (store.currentIndex < store.schedules.length - 1) {
        store.currentIndex++
    }
}
</script>

<template>
    <div class="card shadow-sm h-100">
        <div class="card-body">
            <div v-if="store.schedules.length > 0">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="card-title mb-0">Schedule Preview</h5>
                    <div class="d-flex align-items-center gap-3">
                        <button class="btn btn-outline-secondary btn-sm" @click="decrement" :disabled="store.currentIndex === 0">&laquo; Prev</button>
                        <span class="text-muted small">{{ store.currentIndex + 1 }} of {{ store.schedules.length }}</span>
                        <button class="btn btn-outline-secondary btn-sm" @click="increment" :disabled="store.currentIndex === store.schedules.length - 1">Next &raquo;</button>
                    </div>
                </div>

                <ScheduleGrid :schedule="store.schedules[store.currentIndex]" />
            </div>
            <div v-else class="text-center text-muted py-5">
                <p class="mb-0">No schedules yet — add some courses and hit Fetch Courses.</p>
            </div>
        </div>
    </div>
</template>