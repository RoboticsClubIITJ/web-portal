<template lang="pug">
  div(id ="banners")
    div(class="wrapper" id="banner1")
        div(class="wrapper-background"
            :style= "{ '--hero-image': `url(${HeroImg})` }"
            v-if="!$vuetify.breakpoint.mobile"
          )
        div(class="wrapper-background"
          :style= "{ '--hero-image': `url(${HeroImgMobile})` }"
          v-if="$vuetify.breakpoint.mobile"
        )
        v-main(class="h-100")
          v-row(class="h-100")
            v-col(class="h-100"
              cols=12
              lg=12
              md=6
            )
    div(class="wrapper" id = "banner2")
        div(class="wrapper-background"
            :style= "{ '--hero-image': `url(${HeroImg2})` }"
          )
        div(class="wrapper-content")
    div(class="wrapper" id="banner3")
      v-main(class="h-100 transparent")
        v-row(class="h-100")
          v-col(class="h-100"
            cols=12
            lg=6
            md=12
          )
          v-col(class="h-100"
            cols=12
            lg=6
            v-if="!$vuetify.breakpoint.mobile"
          )
            v-img(
              height="100%"
              width="85%"
              :src="BrainImg"
            )
</template>
<script>
import HelloWorld from '../components/HelloWorld'
import HeroImg from '../assets/bg-2.jpg'
import HeroImgMobile from '../assets/bg-2m.jpg'
import HeroImg2 from '../assets/bg-1.jpg'
import BrainImg from '../assets/robot-3.png'
export default {
  name: 'HomeTop',
  components: {
    HelloWorld
  },
  data: () => ({
    HeroImg,
    HeroImgMobile,
    HeroImg2,
    BrainImg
  })
}
</script>
<style scoped>
  .h-100{
    height: 100%;
    overflow: visible;
  }
  #banners{
    overflow: hidden;
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
  .wrapper-content-img{
    visibility: visible;
    animation-delay: 0.5s;
    animation-name: fadeInUp;
    box-sizing: border-box;
    max-width: 100%;
    height: auto;
    position: relative;
    margin-right: auto;
    margin-left: auto;
  }
</style>
