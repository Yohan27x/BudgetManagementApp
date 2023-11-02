import { createApp } from 'vue'


import App from './App.vue'

import router from '@/router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

createApp(App)


.use(router)

.mount('#app')

