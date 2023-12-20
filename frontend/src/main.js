import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import VueSmoothScroll from 'vue3-smooth-scroll'
import router from './routes'

import Button from './components/Button.vue'
import LinkButton from './components/LinkButton.vue'

let app = createApp(App)

app.use(VueSmoothScroll)

app.component('Button', Button)
app.component('LinkButton', LinkButton)

app.use(router).mount('#app')