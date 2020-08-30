<template lang="pug">
  div
    v-carousel-item(v-for="card in Carousel")
      v-card(@click="showDialog(card)")
        v-img(
          :src="card.img_tile.pathname"
          class="white--text align-end" height="300px"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)")
            v-card-title {{card.title}}
      v-dialog.elevation-12( v-model="dialog"
      max-width="500")
        v-card(v-if="event")
          v-card-title(class="primary darken-1 white--text").justify-center
            v-spacer
            span.ml-4 {{event.title}}
            v-spacer
            v-btn(icon dark @click="dialog = false")
              v-icon mdi-close-circle
          v-card-text
            v-container
              v-layout(row).text-center
                v-flex.md12
                  v-img(v-if="event.img_tile" :src="event.img_tile.pathname" max-height="230" alt="Image" cover).elevation-10
                v-flex.md6.mt-6.text-center
                  v-icon.mb-1(left) mdi-calendar
                  | {{event.date}}
                v-flex.md6.mt-6.text-center
                  a(:href="event.url" v-if="event.url" style="text-decoration: none")
                    v-icon.mb-1(left) mdi-link
                    | {{event.url_name ? event.url_name : 'Link'}}
                v-flex.md12.mt-5
                  p {{event.description ? event.description : ''}}
</template>
<script>
export default {
  name: 'CarouselCard',
  props: {
    Carousel: {
      type: Array,
      required: true
    }
  },
  data: () => ({
    event: null,
    dialog: false
  }),
  mounted () {
    this.Carousel.forEach(element => {
      element.img_tile = new URL(element.img_tile)
      const dt = new Date(element.date)
      element.date = dt.toDateString()
    })
  },
  methods: {
    showDialog (event) {
      this.dialog = true
      this.event = event
    }
  }
}
</script>
