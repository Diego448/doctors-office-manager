import { createRouter, createWebHistory } from 'vue-router'
import DoofmanHome from '../views/DoofmanHome.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: DoofmanHome
    }
  ]
})

export default router
