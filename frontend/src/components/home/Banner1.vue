<template lang="pug">
div.wrapper
  div(class="wrapper-background"
    :style= "{ '--hero-image': `url(${ !$vuetify.breakpoint.mobile ? HeroImg : HeroImgMobile})` }"
    )
    v-row.h-100
      v-col.h-100.d-flex(
          cols=12
          lg=7
          md=12
      )
        div.flex-column(style="margin: auto" v-if= "!$vuetify.breakpoint.mobile")
          div.pa-3.welcome-text {{ WelcomeText }}
          div.d-flex.justify-center.mb-5
            div.mx-4(v-for="logo in logos")
              v-img(:src="logo" width="100px" height="100px")
          p.pa-3.welcome-quote {{WelcomeQuote}}
        div.flex-column.mt-16(style="width:100%" v-if= "$vuetify.breakpoint.mobile")
          div.pa-7.mb-2.welcome-text(style= "font-size: 35px") {{WelcomeText}}
          div(style="bottom:0;position: absolute;")
            div.d-flex.justify-center.mb-1
              div.mx-4(v-for="logo in logos")
                v-img(:src="logo" width="50px" height="50px")
            div.welcome-quote(style="width:100%;" class="text-center pa-3") {{WelcomeQuote}}
</template>
<script>
import HeroImg from '@/assets/bg-2.jpg'
import HeroImgMobile from '@/assets/bg-2m.jpg'
import IitjImg from '@/assets/iitj.png'
import GymImg from '@/assets/gymkhana-logo.png'
import TechImg from '@/assets/tech.png'
export default {
  name: 'Banner1',
  data: () => ({
    HeroImg,
    HeroImgMobile,
    logos: [IitjImg, GymImg, TechImg],
    WelcomeText: 'WELCOME TO ROBOTICS CLUB IITJ',
    WelcomeQuote: '"The best way to predict the future is to invent it"'
  })
}
</script>
<style scoped>
  *{
     font-family: "Lucida Console", Courier, monospace;
     font-weight: bold;
   }
  .logos{
    height: 100px;
    width: 100px;
  }
  .welcome-quote{
    font-size: 18px;
    color: #fff;
    margin-bottom: 30px;
    text-align: center;
  }
  .welcome-text{
    text-align: center;
    font-size: 50px;
    font-weight: 500;
    margin-bottom: 20px;
    color: #fff;
    line-height: 1.4;
  }
  .h-100{
    height: 100%;
    overflow: visible;
  }
  .wrapper {
    overflow: visible;
    position: relative;
    background: color 1c 1a 17;
    padding: 0;
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
