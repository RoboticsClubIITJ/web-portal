<template lang="pug">
    div
      v-main.h-100.transparent
        v-row.h-100
          v-col.h-100.flex-column(
            cols=12
            lg=6
            md=12
          )
            div.d-flex.justify-center
              div.dream-dots(v-for= "color in DotColors" :class="color")
            div.welcome-text.pa-4 About Us
            p.pa-8 {{AboutUs}}
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
import BrainImg from '@/assets/robot-3.png'
export default {
  name: 'Banner3',
  components: {
  },
  data: () => ({
    BrainImg,
    DotColors: ['red', 'green', 'blue', 'purple', 'orange', 'yellow'],
    AboutUs: 'The mission of IIT Jodhpur\'s Robotics Club is to unite students in an educational environment and provide students a place to pursue their interest in mechanical, electronic, and software design by working on large and small scale robotics projects. Having said that we take pride in talking about our projects, be it autonomous bots, humanoids, swarm of tiny robots, robotic arms or aerial vehicles, we haven\'t left any stone unturned. However, the club provides much more than just technical growth to its members, from team-building to cooperation, from perseverance to sincerity, the club teaches you a myriad of interpersonal skills essential in daily life. The club is open to students with or without experience because, believe it or not, none of us had any idea of robotics when we first stepped into the club room, neither do we expect anything from you. You just need to show up and the club and its people will take care of the rest. The club\'s environment perpetuates the sharing of wisdom and experience amongst our members. We cater to every individual who ever wanted to design their own circuit and control their own bot. All we need from you is enthusiasm!'
  })
}
</script>
<style scoped>
  p{
    line-height: 1.9;
    color: rgba(255,255,255,0.5);
    font-size: 17px;
  }
  .dream-dots{
    width: 8px;
    height: 8px;
    background-color: #fff;
    border-radius: 50%;
    margin-right: 5px;
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
