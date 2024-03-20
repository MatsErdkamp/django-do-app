import { createRouter, createWebHistory } from 'vue-router'

import ChargeView from '../views/ChargeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'charge',
      component: ChargeView
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
