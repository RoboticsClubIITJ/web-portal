<template lang="pug">
      Notfound
</template>
<script>
import Notfound from '@/components/Notfound'
export default {
  name: 'PageNotFound',

  components: {
    Notfound
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
