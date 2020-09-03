import Vue from 'vue'
import Vuex from 'vuex'
import { instance } from '@/api/axios'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    user: null,
    userProfile: null
  },
  mutations: {
    LOGIN_FAILURE (state, error) {
      state.error = error
    },
    LOGIN_SUCCESS (state, { user, userProfile }) {
      state.error = null
      state.user = user
      state.userProfile = userProfile
      state.isAuthenticated = true
    },
    LOGOUT (state) {
      state.isAuthenticated = false
      state.user = null
      state.userProfile = null
    }
  },
  actions: {
    logout ({ commit }) {
      return instance.get('/auth/logout').then(() => {
        commit('LOGOUT')
      })
    },
    CheckAuthentication ({ commit }, next) {
      instance.get('/auth/auth-check')
        .then(response => {
          const user = response.data.user
          var userProfile = null
          if (response.data.userprofile) userProfile = response.data.userprofile
          commit('LOGIN_SUCCESS', { user, userProfile })
          if (userProfile === null) router.push({ name: 'CreateProfile' })
          next()
        })
        .catch(error => {
          commit('LOGIN_FAILURE', error)
          router.push({ name: 'Login' })
        })
    }
  },
  modules: {
  }
})
