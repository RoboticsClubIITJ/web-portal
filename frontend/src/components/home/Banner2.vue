<template lang="pug">
  div.wrapper
      div(class="wrapper-background"
          :style= "{ '--hero-image': `url(${HeroImg})` }"
        )
      div.wrapper-content
</template>
<script>
import HeroImg from '@/assets/bg-1.jpg'
export default {
  name: 'Banner2',
  components: {
  },
  data: () => ({
    HeroImg
  })
}
</script>
<style scoped>
  .h-100{
    height: 100%;
    overflow: visible;
  }
  .wrapper {
    overflow: visible;
    position: relative;
    background: color 1c 1a 17;
    padding: 0;
    /* -webkit-transition-property: height;
    -webkit-transition-duration: 0.3s; */
    transition-timing-function: ease-in;
    box-sizing: border-box;
    width: 100vw !important;
    height: 100vh !important;
    z-index: 1;
  }
  .wrapper-background{
    width: 101%;
    height: 100%;
    background-image: var(--hero-image);
    box-sizing: border-box;
    background-size: cover;
    background-position: center center;
  }
  .wrapper-content{
    background: rgb(33,0,67,0.9);
    width: 100%;
    height: 100%;
    position: absolute !important;
    top: 0;
    left: 0;
    z-index: 10;
    overflow: visible;
  }
</style>
