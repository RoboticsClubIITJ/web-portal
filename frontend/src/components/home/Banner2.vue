<template lang="pug">
  div.wrapper
    v-layout(row).wrapper-content
      v-flex.md6.xs12
        div(style="height: 25%")
        v-carousel.home-carousel( height="300px" v-if="Carousel.length"
          cycle hide-delimiter-background show-arrows-on-hover)
          CarouselCard(:Carousel="Carousel")
      v-flex.md5.elevation-0(flat tile depressed).pl-md-5.xs12
        div(style="height: 20%")
        v-card-title.headline.justify-center
          v-icon(left large color="white") mdi-newspaper-plus
          h3(style="color: white") Activities and News
        v-tabs(fixed-tabs background-color='rgb(57,73,171)' dark v-model="tab")
          <v-tabs-slider color="rgb(57,73,171)"></v-tabs-slider>
          v-tab
            v-icon(left) mdi-lightbulb-outline
            | Upcoming Events
          v-tab
            v-icon(left) mdi-newspaper
            | News
        v-tabs-items(v-model="tab" )
          v-tab-item
            v-card(flat tile text ).pa-4.transparent
                  v-card-text(v-if="UpcomingEvents.length")
                    NewsTable(:newsList="UpcomingEvents")
                  v-card-text(v-else).pa-4.title.text-center There are no Events
          v-tab-item
            v-card(flat tile text ).pa-4.background-color
              v-card-text(v-if="News.length")
                NewsTable(:newsList="News")
              v-card-text(v-else).pa-4.title.text-center There is no news currently
    center(style="width:100%;bottom:0;position:absolute;")
      v-img(:src= "ShapeImg" width="15%")
</template>
<script>
import HeroImg from '@/assets/bg-1.jpg'
import NewsTable from '@/components/home/NewsTable'
import CarouselCard from '@/components/home/CarouselCard'
import ShapeImg from '@/assets/shape1.png'
import { instance } from '@/api/axios'
export default {
  name: 'Banner2',
  components: {
    NewsTable,
    CarouselCard
  },
  data: () => ({
    HeroImg,
    ShapeImg,
    tab: null,
    UpcomingEvents: [],
    News: [{ title: 'aman', date: '2015', link: 'https://google.com' }],
    Carousel: []
  }),
  async created () {
    try {
      const carousel = await instance.get('/general_assets/homecarousel')
      const news = await instance.get('/general_assets/news')
      const events = await instance.get('/general_assets/upcomingevents')
      this.Carousel = carousel.data
      this.News = news.data
      this.UpcomingEvents = events.data
    } catch (e) {
      console.log(e)
    }
  }
}
</script>
<style scoped>
  .home-carousel{
    width: 80%;
    border-radius:10%;
    margin: auto
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
    width: 100%;
    height: 100%;
    position: absolute !important;
    top: 0;
    left: 0;
    z-index: 10;
    overflow: visible;
    margin: 0;
  }
</style>
