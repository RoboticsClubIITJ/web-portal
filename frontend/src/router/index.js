import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Comingsoon from '../views/Comingsoon.vue'
import PageNotFound from '../views/PageNotFound.vue'
import CreateProfile from '../views/CreateProfile.vue'
import About from '../components/home/Banner3.vue'

import { instance } from '../api/axios'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { loader: true }
  },
  {
    path: '*',
    name: 'Pagenotfound',
    component: PageNotFound
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/team',
    name: 'Team',
    component: Comingsoon
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Comingsoon
  },
  {
    path: '/competitions',
    name: 'Competitions',
    component: Comingsoon
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
    component: Comingsoon,
    meta: { NoFooter: true, NoAppBar: true, NoBackground: true },
    beforeEnter (to, from, next) {
      AuthCheck(next)
    }
  },
  {
    path: '/create-profile',
    name: 'CreateProfile',
    component: CreateProfile,
    meta: { NoFooter: true, NoAppBar: true, NoBackground: true }
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
