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
        v-btn.pa-3.ma-5(text v-if="!$vuetify.breakpoint.mobile && !user" key="sub" @click="" :to="'/studentzone'" exact) StudentZone
        v-menu(open-on-hover offset-y v-if="!$vuetify.breakpoint.mobile && user")
          template(v-slot:activator="{ on, attrs }").mt-5
            v-btn.pa-3.ma-5(@click="" :to="'/studentzone'" v-bind="attrs" v-on="on" color="transparent")
              v-icon.mr-4 mdi-account
              | {{user.first_name}}
              v-icon.ml-4 mdi-menu-down
          v-list(rounded color="blue darken-4").mt-5
            center
              v-avatar(size = "70").pt-1
                v-img(:src="userprofile.avatar")
            v-divider
            v-list-item(v-for="item in login_items" :key="item.text" @click="" :to="item.router" exact)
              v-list-item-action.mr-3
                v-icon.white--text {{item.icon}}
              v-list-item-content
                v-list-item-title.white--text {{item.text}}
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
        v-list-item(v-if="!user" @click="" to="/studentzone" exact)
          v-list-item-action
            v-icon.white--text mdi-account
          v-list-item-content
            v-list-item-title.white--text Student Zone
        v-list-item(v-if="user" v-for="item in login_items" :key="item.text" @click="" :to="item.router" exact)
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
    user: null,
    userprofile: null,
    items: [
      { text: 'Home', icon: 'mdi-home', router: '/' },
      { text: 'About', icon: 'mdi-information', router: '/about' },
      { text: 'Projects', icon: 'mdi-briefcase-edit-outline', router: '/projects' },
      { text: 'Competitions', icon: 'mdi-briefcase-edit-outline', router: '/competitions' },
      { text: 'Resources', icon: 'mdi-shopping', router: '/resources' },
      { text: 'Team', icon: 'mdi-human-male-male', router: '/team' }
    ],
    login_items: [
      { text: 'My Profile', icon: 'mdi-account', router: '/studentzone' },
      { text: 'Edit Profile', icon: 'mdi-pencil', router: '/studentzone/editprofile' },
      { text: 'Leveling', icon: 'mdi-school', router: '/studentzone/leveling' },
      { text: 'Inventory', icon: 'mdi-shopping', router: '/inventory' },
      { text: 'Logout', icon: 'mdi-logout', router: '/logout' }
    ]
  }),
  created () {
    this.userprofile = this.$store.state.userProfile
    this.user = this.$store.state.user
  },
  methods: {
    BarScroll (e) {
      var scroll = e.target.scrollingElement.scrollTop
      this.BarColor = scroll > 100 ? 'indigo darken-1' : 'transparent'
    }
  }
}
</script>
