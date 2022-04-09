import { createRouter, createWebHistory } from 'vue-router'
import DoofmanHome from '../views/DoofmanHomeView.vue'
import LoginView from '../views/LoginView.vue'
import PatientsView from '@/views/PatientsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: DoofmanHome
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/patients',
      name: 'patients',
      component: PatientsView
    }
  ]
})

export default router
