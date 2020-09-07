import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Comingsoon from '../views/Comingsoon.vue'
import PageNotFound from '../views/PageNotFound.vue'
import About from '../components/home/Banner3.vue'
import Competetions from '../components/Competetions.vue'
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
    path: '/competetions',
    name: 'Competetions',
    component: Competetions
  },
  {
    path: '/resources',
    // redirect to drive
    beforeEnter () {
      window.location = 'https://drive.google.com/drive/u/1/folders/1TMZxnLB4Fp9LztqkkzKcpaM5b-H7S8lI'
    }
  },
  {
    path: '/login',
    name: 'Login',
    // redirect to Google Login
    beforeEnter () {
      window.location = '/api/auth/login'
    }
  },
  {
    path: '/studentzone',
    name: 'StudentZone',
    component: Comingsoon,
    meta: { NoAP: true },
    beforeEnter (next) {
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
