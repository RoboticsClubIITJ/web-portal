<template lang="pug">
  v-simple-table.elevation-4
    thead(class="primary lighten-1 gray--text")
      th.pr-0.pl-4.text-left(style="width: 10%")
        v-icon mdi-pen
      th.subtitle-1.text-left.pl-4 Title
      th.subtitle-1.text-center
        v-icon mdi-calendar
    tbody
      tr(v-for="(news,i) in newsList" :key="i" @click.stop="showDialog(news)")
        td
          v-icon mdi-chevron-right
        td {{news.title}}
        td.text-center {{ news.date }}
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
                | {{event.date}}&nbsp;&nbsp;{{event.time}}
              v-flex.md6.mt-6.text-center
                a(:href="event.url" v-if="event.url" style="text-decoration: none")
                  v-icon.mb-1(left) mdi-link
                  | {{event.url_name ? event.url_name : 'Link'}}
              v-flex.md12.mt-5
                p {{event.description ? event.description : ''}}
</template>

<script>
export default {
  name: 'NewsTable',
  props: {
    newsList: {
      type: Array,
      required: true
    }
  },
  data: () => ({
    event: null,
    dialog: false
  }),
  created () {
    this.newsList.forEach(news => {
      news.img_tile = new URL(news.img_tile)
      const dt = new Date(news.date)
      news.date = dt.toDateString()
      news.time = dt.toLocaleTimeString()
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
