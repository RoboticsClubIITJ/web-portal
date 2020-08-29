<template lang="pug">
  v-simple-table.elevation-4
    thead(class="primary lighten-1 gray--text")
      th.pr-0.pl-4.text-left(style="width: 10%")
        v-icon mdi-pen
      th.subtitle-1.text-left.pl-4 Title
      th.subtitle-1.text-center
        v-icon mdi-calendar
    tbody
      tr(v-for="(node,i) in newsList" :key="i" @click.stop="showDialog(node)")
        td
          v-icon mdi-chevron-right
        td {{node.title}}
        td.text-center {{ node.date }}
    v-dialog.elevation-12( v-model="dialog"
      max-width="500")
      v-card(v-if="singleEvent")
        v-card-title(class="primary darken-1 white--text").justify-center
          v-spacer
          span.ml-4 {{singleEvent.title}}
          v-spacer
          v-btn(icon dark @click="dialog = false")
            v-icon mdi-close-circle
        v-card-text
          v-container
            v-layout(row).text-center
              v-flex.md12
                v-img(v-if="singleEvent.banner" :src="singleEvent.banner" max-height="230" alt="Image" cover).elevation-10
              v-flex.md6.mt-6.text-center
                v-icon.mb-1(left) mdi-calendar
                | {{singleEvent.date}}
              v-flex.md6.mt-6.text-center
                a(:href="singleEvent.link" v-if="singleEvent.link" style="text-decoration: none")
                  v-icon.mb-1(left) mdi-link
                  | Link
              v-flex.md12.mt-5
                p {{singleEvent.discrption ? singleEvent.discrption : ''}}
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
    singleEvent: null,
    dialog: false
  }),
  methods: {
    showDialog (event) {
      console.log('ll')
      this.dialog = true
      this.singleEvent = event
    }
  }
}
</script>
