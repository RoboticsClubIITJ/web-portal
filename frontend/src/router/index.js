import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Comingsoon from '../views/Comingsoon.vue'
import PageNotFound from '../views/PageNotFound.vue'
import CreateProfile from '../views/CreateProfile.vue'
import UpdateProfile from '../components/UpdateProfile.vue'
import About from '../components/home/Banner3.vue'
import Team from '../views/Team.vue'
import Projects from '../views/Projects.vue'
import StudentZone from '../views/StudentZone.vue'
import Competitions from '../views/Competitions.vue'
import Profile from '../components/Profile.vue'
import Leveling from '../components/Leveling.vue'
import CompCard from '../components/CompCard.vue'

import store from '@/store'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { Footer: true, AppBar: true, Background: true }
  },
  {
    path: '*',
    name: 'Pagenotfound',
    component: PageNotFound,
    meta: { Footer: true, AppBar: true, Background: true }
  },
  {
    path: '/about',
    name: 'About',
    meta: { Footer: true, AppBar: true, Background: true },
    component: About
  },
  {
    path: '/team',
    name: 'Team',
    meta: { Footer: true, AppBar: true, Background: true },
    component: Team
  },
  {
    path: '/projects',
    name: 'Projects',
    meta: { Footer: true, AppBar: true, Background: true },
    component: Projects
  },
  {
    path: '/competitions',
    name: 'Competitions',
    meta: { Footer: true, AppBar: true, Background: true },
    component: Competitions
  },
  {
    path: '/resources',
    // redirect to drive
    beforeEnter (to, from, next) {
      window.location =
        'https://drive.google.com/drive/u/1/folders/1TMZxnLB4Fp9LztqkkzKcpaM5b-H7S8lI'
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
    path: '/logout',
    name: 'Logout',
    // redirect to Google Login
    beforeEnter (to, from, next) {
      store.dispatch('logout')
    }
  },
  {
    path: '/studentzone',
    name: 'StudentZone',
    meta: { Footer: true, AppBar: true, Background: true },
    component: StudentZone,
    beforeEnter (to, from, next) {
      if (store.state.isAuthenticated && store.state.userProfile != null) {
        next()
      } else {
        store.dispatch('CheckAuthentication', next)
      }
    },
    children: [
      {
        path: '/',
        component: Profile,
        meta: { Footer: true, AppBar: true, Background: true }
      },
      {
        path: 'editprofile',
        component: UpdateProfile,
        meta: { Footer: true, AppBar: true, Background: true }
      },
      {
        path: 'leveling',
        component: Leveling,
        meta: { Footer: true, AppBar: true, Background: true }
      },
      {
        path: 'competitions/:id',
        component: CompCard,
        meta: { Footer: true, AppBar: true, Background: true }
      }
    ]
  },
  {
    path: '/inventory',
    name: 'Inventory',
    meta: { Footer: false, AppBar: true, Background: true },
    component: Comingsoon,
    beforeEnter (to, from, next) {
      if (store.state.isAuthenticated && store.state.userProfile != null) {
        next()
      } else {
        store.dispatch('CheckAuthentication', next)
      }
    }
  },
  {
    path: '/create-profile',
    name: 'CreateProfile',
    component: CreateProfile,
    beforeEnter (to, from, next) {
      if (store.state.isAuthenticated && store.state.userProfile === null) {
        next()
      } else {
        next({ name: 'StudentZone' })
      }
    }
  }
  /* {
    path: '/update-profile',
    name: 'UpdateProfile',
    component: UpdateProfile,
    meta: { Footer: true, AppBar: true, Background: true },
    beforeEnter (to, from, next) {
      if (!store.state.isAuthenticated) {
        next()
      } else {
        next({ name: 'StudentZone' })
      }
    }
  } */
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
