<template lang="pug">
  div.main-wrapper
    div.banners
      Banner1
      Banner2
      Banner3
    Team
</template>
<script>
import Banner1 from '@/components/home/Banner1'
import Banner2 from '@/components/home/Banner2'
import Banner3 from '@/components/home/Banner3'
import Team from '@/components/home/Team'
export default {
  name: 'Home',

  components: {
    Banner1,
    Banner2,
    Banner3,
    Team
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
