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
    v-navigation-drawer(color="blue darken-4"
      v-model="drawer"
      left
      app
    )
      div ekfnefdnedwek
</template>
<script>
import Logo from '../assets/robologo.svg'
export default {
  name: 'AppBar',
  data: () => ({
    BarColor: 'transparent',
    drawer: false,
    Logo
  }),
  methods: {
    BarScroll (e) {
      var scroll = e.target.scrollingElement.scrollTop
      this.BarColor = scroll > 100 ? 'indigo darken-1' : 'transparent'
    }
  }
}
</script>
