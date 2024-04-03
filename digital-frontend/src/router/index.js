import { createRouter, createWebHistory } from 'vue-router'

import ChargeView from '../views/ChargeView.vue'
import CircleView from '../views/CircleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'charge',
      component: ChargeView
    },
    {
      path: '/circle',
      name: 'circle',
      component: CircleView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/DashboardView.vue')
    },

    {
      path: '/counter',
      name: 'counter',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/CounterView.vue')
    },
    {
      path: '/charge',
      name: 'charge',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ChargeView.vue')
    }
  ]
})

export default router
