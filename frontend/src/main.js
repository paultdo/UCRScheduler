import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { inject } from '@vercel/analytics'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'

inject()

const app = createApp(App)

app.use(createPinia())
app.mount('#app')
