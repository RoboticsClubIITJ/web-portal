<template lang="pug">
  div
    v-container.text-center
      h1.header.my-16
        | LEVELING SYSTEM
    v-container.text-center
      v-tabs(fixed-tabs background-color="indigo" dark v-model="tab")
        v-tab(v-for="(key,i) in Object.keys(deps)" :key="i")
          | {{key}}
      v-tabs-items(v-model="tab")
        v-tab-item(v-for="(key,i) in Object.keys(deps)" :key="i")
          v-card(background-color="white" flat)
            v-expansion-panels(focusable)
              v-expansion-panel(v-for="item in deps[key]" :key="item.id" :disabled="item.status != 'Next'")
                v-expansion-panel-header
                  | {{item.title}}
                  div.text-right
                    v-chip(color="success" text-color="white" style="width: 12%" v-if="item.status == 'Approved'").ma-2
                      v-avatar(left)
                        v-icon mdi-checkbox-marked-circle
                      | Approved
                    v-chip(color="grey" text-color="white" style="width: 12%" v-if="item.status == 'Pending'").ma-2
                      v-avatar(left)
                        v-icon mdi-comment-processing
                      | Pending
                    v-chip(color="red" text-color="white" style="width: 12%" v-if="item.status == 'Rejected'").ma-2
                      v-avatar(left)
                        v-icon mdi-comment-remove-outline
                      | Rejected
                    v-chip(color="tale" text-color="white" style="width: 12%" v-if="!item.status").ma-2
                      v-avatar(left)
                        v-icon mdi-lock
                      | Locked
                v-expansion-panel-content.ma-2
                  | {{item.description}}
                  v-btn(primary @click="push(item.form_link)").ma-4
                   | Submit
</template>
<script>
import { instance } from '@/api/axios'
export default {
  name: 'Leveling',
  data: () => ({
    tab: null,
    deps: {}
  }),
  async created () {
    const res = await instance.get('/leveling/departments/')
    var data = res.data
    this.deps = data.departments
    Object.entries(this.deps).forEach(([key, value]) => {
      for (var item in value) {
        var val = value[item]
        if (val.status === 'Approved') {
          continue
        }
        if (!val.status) {
          this.deps[key][item].status = 'Next'
        }
        break
      }
    })
  },
  methods: {
    push (url) {
      window.location.href = url
    }
  }
}
</script>
