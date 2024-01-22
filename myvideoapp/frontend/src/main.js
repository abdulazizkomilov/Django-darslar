// main.js
// import './assets/css/all.min.css'
// import './assets/css/apexcharts.css'
// import './assets/css/bootstrap-icons.css'
// import './assets/css/overlayscrollbars.min.css'
// import './assets/css/style.css'

import './assets/css/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
