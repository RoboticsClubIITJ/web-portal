<template lang="pug">
div.wrapper
  div(class="wrapper-background"
    :style= "{ '--hero-image': `url(${ HeroImg })` }"
    )
    v-row.h-100
      div.btns
        v-btn(rounded style = "padding: 20px;font-size: 20px;color: white;margin-right: 30px;" color="primary")
          a(class="white--text text-decoration-none" :href="`/django_media/uploads/Rulebook_for_Thinkathon_2021.pdf`") Rules
        v-btn(rounded style = "padding: 20px;font-size: 20px;color: white" color="primary")
          a(class="white--text text-decoration-none" :href="`/competitions`") Register
      div.flex-column(style="margin: auto;margin-bottom: 130px" v-if= "!$vuetify.breakpoint.mobile")
        div.d-flex(style="width: 300px;margin: auto;padding-bottom:40pxmargin-top: 0;")
          v-img(
            transition="fade-transition"
            :src="Logo"
          )
        div.pt-4.welcome-text {{ WelcomeText }}
        p.welcome-date {{Dates}}
        div(style="padding-top: 40px;color: #fff")
          | Registration starts in
        div.d-flex.justify-center.mb-5(style="padding-top: 20px")
          span.mx-4.welcome-text {{days}} : {{hours}} : {{minutes}} : {{seconds}}
</template>
<script>
import HeroImg from '@/assets/d1.jpg'
import Logo from '../assets/robologo.svg'
export default {
  name: 'Thinkathon',
  data: () => ({
    Logo,
    HeroImg,
    /* logos: [IitjImg, GymImg, TechImg], */
    WelcomeText: 'THINKATHON 2021',
    WelcomeQuote: '"The best way to predict the future is to invent it"',
    Dates: '16Feb - 23Feb',
    now: Math.trunc((new Date()).getTime() / 1000),
    date: '2021-02-15 23:59:59'
  }),
  mounted () {
    window.setInterval(() => {
      this.now = Math.trunc((new Date()).getTime() / 1000)
    }, 1000)
  },
  computed: {
    dateInMilliseconds () {
      return Math.trunc(Date.parse(this.date) / 1000)
    },
    seconds () {
      return (this.dateInMilliseconds - this.now) % 60
    },
    minutes () {
      return Math.trunc((this.dateInMilliseconds - this.now) / 60) % 60
    },
    hours () {
      return Math.trunc((this.dateInMilliseconds - this.now) / 60 / 60) % 24
    },
    days () {
      return Math.trunc((this.dateInMilliseconds - this.now) / 60 / 60 / 24)
    }
  }
}
</script>
<style scoped>
  *{
     font-family: "Lucida Console", Courier, monospace;
     font-weight: bold;
   }
   .btns{
     padding-top: 50px;
     padding-bottom: 50px;
     padding-left: 70%;
     position: relative;
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
  .welcome-date{
    font-size: 18px;
    color: #fff;
    margin-bottom: 50px;
    text-align: center;
  }
  .welcome-text{
    text-align: center;
    font-size: 60px;
    font-weight: 700;
    margin-bottom: 3px;
    margin-top: 12px;
    color: #fff;
    line-height: 1.4;
  }
  .h-100{
    height: 100%;
    overflow: visible;
  }
  .wrapper {
    overflow: hidden;
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
