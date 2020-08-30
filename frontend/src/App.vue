<template lang="pug">
  v-app
    div.main-content-wrapper
      AppBar(v-if="!$route.meta.NoAP")
      router-view
      Footer(v-if="!$route.meta.NoAP")
</template>

<script>
import AppBar from './components/AppBar'
import HomeTop from './components/HomeTop'
import HelloWorld from './components/HelloWorld'
import Details from './components/Details'
import Footer from './components/Footer'
export default {
  name: 'App',

  components: {
    AppBar,
    HomeTop,
    HelloWorld,
    Details,
    Footer
  },

  data: () => ({
  })
}
</script>
<style>
  .main-content-wrapper{
    padding:0;
    background: linear-gradient(180deg,#240044 0,#0f0240 25%,#400959 40%,#0f0240 65%,#0f0240);
  }
</style>
