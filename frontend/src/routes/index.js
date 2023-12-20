import { createRouter, createWebHistory } from 'vue-router'

const Home = () => import('../views/Home.vue')

const routes = [
  { path: '/', component: Home },
  { path: '/architects', component: () => import('../views/Architects.vue') },
  { path: '/architects/:id', component: () => import('../views/Architect.vue') },
  { path: '/projects', component: () => import('../views/Projects.vue') },
  { path: '/projects:id', component: () => import('../views/Project.vue') },
  // { path: '/project:id', component: () => import('../') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router