<script setup>
    import { useSchedulesStore } from '../stores/schedule';
    import ScheduleGrid from './ScheduleGrid.vue';
    const store = useSchedulesStore()
    

    function decrement() {
        if(store.currentIndex > 0) {
            store.currentIndex--
        }
    }

    function increment() {
        if(store.currentIndex < store.schedules.length - 1) {
            store.currentIndex++
        }
    }
</script>

<template>
    <div v-if="store.schedules.length > 0">
        <ul>
            <li v-for="(bundle, index) in store.schedules[store.currentIndex]" :key="index">
                <ul>
                    <li v-for="section in bundle" :key="section.id">
                        {{ section.crn }}
                    </li>
                </ul>
            </li>
        </ul>

        <ScheduleGrid :schedule="store.schedules[store.currentIndex]" />
    </div>
    <div v-else>
        <p>No schedules yet!</p>
    </div>
    <div>
        <button class="btn btn-secondary" @click="decrement" :disabled="store.currentIndex === 0"><<</button>
        <p>{{ store.currentIndex + 1 }} of {{ store.schedules.length }}</p>
        <button class="btn btn-secondary" @click="increment" :disabled="store.currentIndex === store.schedules.length - 1">>></button>
    </div>

</template>