<template lang="pug">
  div.wrapper(
    :style= "{ '--hero-image': `url(${HeroImg}) no-repeat` }"
  )
    div.container
</template>
<script>
import HeroImg from '@/assets/footer-bg1.png'
export default {
  name: 'Footer',
  data: () => ({
    HeroImg
  })
}
</script>
<style scoped>
  .wrapper{
    background: var(--hero-image);
    background-size: cover;
    padding: 80px 0;
    margin-top: 100px;
    margin: 0;
    box-sizing: border-box;
  }
</style>
