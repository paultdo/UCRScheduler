<script setup>
import CourseInput from './components/CourseInput.vue'
import ScheduleBrowser from './components/ScheduleBrowser.vue'
</script>

<template>
    <div class="container-fluid py-4">
        <h1 class="mb-4">UCR Scheduler</h1>
        <div class="row g-4">
            <div class="col-lg-4">
                <CourseInput />
            </div>
            <div class="col-lg-8">
                <ScheduleBrowser />
            </div>
        </div>
    </div>
</template>