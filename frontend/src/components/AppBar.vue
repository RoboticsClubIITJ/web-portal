<template lang="pug">
  div
    v-app-bar(
      app
      dark
      :color="BarColor"
      v-scroll="BarScroll"
    )
      div(class="d-flex")
        v-img(
          transition="fade-transition"
          :src="Logo"
        )
      v-spacer
      v-btn(@click="drawer = !drawer" text v-if="$vuetify.breakpoint.mobile")
          v-icon(large v-if="!drawer") mdi-menu
          v-icon(large v-if="drawer")  mdi-close
      div
        v-btn.pa-3.ma-5(text v-if="!$vuetify.breakpoint.mobile" v-for="item in items" :key="item.text" @click="" :to="item.router" exact) {{item.text}}
    v-navigation-drawer(v-if="$vuetify.breakpoint.mobile"
      color="blue darken-4"
      v-model="drawer"
      left
      app
    )
      v-list(rounded)
        v-list-item( v-for="item in items" :key="item.text" @click="" :to="item.router" exact)
          v-list-item-action
            v-icon.white--text {{item.icon}}
          v-list-item-content
            v-list-item-title.white--text {{item.text}}
</template>
<script>
import Logo from '../assets/robologo.svg'
export default {
  name: 'AppBar',
  data: () => ({
    BarColor: 'transparent',
    drawer: false,
    Logo,
    items: [
      { text: 'Home', icon: 'mdi-home', router: '/' },
      { text: 'About', icon: 'mdi-information', router: '/about' },
      { text: 'Projects', icon: 'mdi-briefcase-edit-outline', router: '/projects' },
      { text: 'Competitions', icon: 'mdi-briefcase-edit-outline', router: '/competitions' },
      { text: 'Resources', icon: 'mdi-shopping', router: '/resources' },
      { text: 'Team', icon: 'mdi-human-male-male', router: '/team' },
      { text: 'Student Zone', icon: 'mdi-account', router: '/studentzone' }
    ]
  }),
  methods: {
    BarScroll (e) {
      var scroll = e.target.scrollingElement.scrollTop
      this.BarColor = scroll > 100 ? 'indigo darken-1' : 'transparent'
    }
  }
}
</script>
