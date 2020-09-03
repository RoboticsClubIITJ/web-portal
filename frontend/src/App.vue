<template lang="pug">
  v-app
    div(:class="$route.meta.NoBackground ? '' : 'main-content-wrapper'")
      AppBar(v-if="!$route.meta.NoAppBar")
      router-view
      Footer(v-if="!$route.meta.NoFooter")
</template>

<script>
import AppBar from '@/components/AppBar'
import Footer from '@/components/Footer'
export default {
  name: 'App',

  components: {
    AppBar,
    Footer
  },

  data: () => ({
  })
}
</script>
<style scoped>
  .main-content-wrapper{
    padding:0;
    background: linear-gradient(180deg,#240044 0,#0f0240 25%,#400959 40%,#0f0240 65%,#0f0240);
  }
</style>
