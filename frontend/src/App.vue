<template lang="pug">
  v-app
    div(:class="!!$route.meta.Background ? 'main-content-wrapper' : ''")
      AppBar(v-if="!!$route.meta.AppBar")
      router-view
      Footer(v-if="!!$route.meta.Footer")
</template>

<script>
import AppBar from '@/components/AppBar'
import Footer from '@/components/Footer'
import { instance } from '@/api/axios'
export default {
  name: 'App',

  components: {
    AppBar,
    Footer
  },

  data: () => ({
  }),

  created () {
    instance.get('/auth/csrf-token/').then(response => {
      const token = response.data.csrftoken
      document.cookie = `csrftoken = ${token}`
    })
  }
}
</script>
<style scoped>
  .main-content-wrapper{
    padding:0;
    background: linear-gradient(180deg,#240044 0,#0f0240 25%,#400959 40%,#0f0240 65%,#0f0240);
  }
</style>
