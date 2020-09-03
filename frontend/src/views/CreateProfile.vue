<template lang="pug">
  div.ma-7
    v-alert( type="info") Please Create Your Profile To Continue
    v-container.elevation-10.pa-10
      v-form(ref="form" v-model="valid")
        div.mx-auto(style="max-width: 200px")
          v-avatar.orange(size="100").mx-14
          v-file-input.pt-4(
          :rules="rules"
          accept="image/png, image/jpeg, image/bmp"
          placeholder="Pick an avatar"
          prepend-icon="mdi-camera"
          label="Avatar")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account"
              :counter="14" label="First Name" :rules="[v => !!v || 'Name is required']"
            )
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account"
              :counter="14" label="Last Name" :rules="[v => !!v || 'Name is required']"
            )
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-email" label="Email" disabled value="mk@")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account-key" label="Roll Number" :rules="[v => !!v || 'Roll Number is required']")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Gender" :items="GenderChoices" :rules="[v => !!v || 'Field is required']")
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Year" :items="YearChoices" :rules="[v => !!v || 'Field is required']")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Programme" :items="ProgChoices" :rules="[v => !!v || 'Field is required']")
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Branch" :items="BranchChoices" :rules="[v => !!v || 'Field is required']")
        center.my-5
          v-divider(width="90%")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-phone" label="Phone Number"
            :rules="[v => (!/[^0-9]/.test(v)) || v.length==0 || 'Enter a valid Number', v => v.length==10 || v.length==0 || 'Enter a valid Number',]")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-linkedin" label="Linkedin Profile LInk"
            :rules="[v => /linkedin.com/.test(v) || v.length==0 || 'Enter a valid link', ]")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-github-circle" label="Linkedin Profile LInk"
            :rules="[v => /github.com/.test(v) || v.length==0 || 'Enter a valid link', ]")
        v-row.justify-center.mx-10.mb-10
          v-combobox( v-model="stack" :items="StackChoices" :search-input.sync="stacksearch"
          hide-selected hint="Select or add new stack in you stack" label="Stack"
          multiple persistent-hint small-chips prepend-icon="mdi-basket-fill")
            <template v-slot:no-data>
              v-list-item
                v-list-item-content
                  v-list-item-title
                    | No results matching "{{ stacksearch }}". Press enter to create a new one
            </template>
        v-row.justify-center
          v-btn.mr-5(:disabled ="!valid" color="sucess" @click="validate") Submit
          v-btn(color="error" @click="reset") Reset
</template>
<script>
import { instance } from '@/api/axios'
export default {
  name: 'CreateProfile',
  data: () => ({
    StackChoices: [],
    GenderChoices: [],
    BranchChoices: [],
    YearChoices: [],
    ProgChoices: [],
    stacksearch: null,
    valid: true
  }),
  async created () {
    const res = await instance.get('/general_assets/profile-selectlist')
    var data = res.data
    this.StackChoices = data.stack
    this.GenderChoices = data.gender
    this.BranchChoices = data.branch
    this.YearChoices = data.year
    this.ProgChoices = data.prog
  },
  methods: {
    validate () {
      this.$refs.form.validate()
    },
    reset () {
      this.$refs.form.reset()
    }
  }
}
</script>
