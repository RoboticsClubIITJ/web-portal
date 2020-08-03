<template lang="pug">
  router-view
</template>

<script>
import AppBar from './components/AppBar'
import HomeTop from './components/HomeTop'
import HelloWorld from './components/HelloWorld'
export default {
  name: 'App',

  components: {
    AppBar,
    HomeTop,
    HelloWorld
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
