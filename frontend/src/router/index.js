import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Team from '../views/Team.vue'

import { instance } from '../api/axios'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/team',
    name: 'Team',
    component: Team
  },
  {
    path: '/resources',
    // redirect to drive
    beforeEnter (to, from, next) {
      window.location = 'https://drive.google.com/drive/u/1/folders/1TMZxnLB4Fp9LztqkkzKcpaM5b-H7S8lI'
    }
  },
  {
    path: '/login',
    name: 'Login',
    // redirect to Google Login
    beforeEnter (to, from, next) {
      window.location = '/api/auth/login'
    }
  },
  {
    path: '/studentzone',
    name: 'StudentZone',
    meta: { NoAP: true },
    beforeEnter (to, from, next) {
      AuthCheck(next)
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

var AuthCheck = async function (next) {
  try {
    await instance.get('/auth/auth-check')
    next()
  } catch (err) {
    next({ name: 'Login' })
  }
}

export default router
