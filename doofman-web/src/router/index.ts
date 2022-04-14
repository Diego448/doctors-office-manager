import { createRouter, createWebHistory } from 'vue-router'
import DoofmanHome from '../views/DoofmanHomeView.vue'
import LoginView from '../views/LoginView.vue'
import PatientsView from '@/views/PatientsView.vue'
import AppointmentsView from '@/views/AppointmentsView.vue'

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
    },
    {
      path: '/appointments/:id',
      name: 'patient-appointments',
      component: AppointmentsView
    },
    {
      path: '/appointments',
      name: 'appointments',
      component: AppointmentsView
    }
  ]
})

export default router
