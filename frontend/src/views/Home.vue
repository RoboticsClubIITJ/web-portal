<template lang="pug">
  div.main-wrapper
    div.banners
      Banner1
      Banner2
      Banner3
    Team
  v-app
    AppBar
    div(class="main-content-wrapper")
      HomeTop
      HelloWorld
      Footer
      Details
</template>
<script>
import Banner1 from '@/components/home/Banner1'
import Banner2 from '@/components/home/Banner2'
import Banner3 from '@/components/home/Banner3'
import Team from '@/components/home/Team'
import AppBar from '@/components/AppBar'
import HomeTop from '@/components/HomeTop'
import HelloWorld from '@/components/HelloWorld'
import Details from '@/components/Details'
import Footer from '@/components/Footer'
export default {
  name: 'Home',

  components: {
    Banner1,
    Banner2,
    Banner3,
    Team,
    AppBar,
    HomeTop,
    HelloWorld,
    Details,
    Footer
  },

  data: () => ({
    drawer: true
  })
}
</script>
<style>
  .main-wrapper{
    padding:0;
  }
  .banners{
    overflow: hidden;
  }
</style>
