<template lang="pug">
  div
    v-container.text-center
      h1.header.my-16
        | EDIT PROFILE
        v-icon(class="mb-1 ml-4" x-large color='white') mdi-pencil
    v-container.elevation-10.pa-10.white
      v-form(ref="form" v-model="valid")
        div.mx-auto(style="max-width: 200px")
          v-avatar(size="100").mx-14
            v-img(:src="cfile ? cfile : dfile")
          v-file-input.pt-4(v-model="file" @change="updatefile"
          accept="image/png, image/jpeg, image/bmp"
          placeholder="Pick an avatar"
          prepend-icon="mdi-camera"
          label="Avatar")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account" v-model="first_name"
              :counter="14" label="First Name" :rules="[v => !!v || 'Name is required']"
            )
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account" v-model="last_name"
              :counter="14" label="Last Name" :rules="[v => !!v || 'Name is required']"
            )
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field(prepend-icon="mdi-email" label="Email" disabled :value="$store.state.user.email")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-account-key" label="Roll Number" v-model="roll_number"
            :rules="[v => !!v || 'Roll Number is required']")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Gender" :items="GenderChoices" v-model="gender"
            :rules="[v => !!v || 'Field is required']")
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Year" :items="YearChoices" v-model="year"
            :rules="[v => !!v || 'Field is required']")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Programme" :items="ProgChoices" v-model="prog"
            :rules="[v => !!v || 'Field is required']")
          v-col(cols=12 lg=4 sm=12)
            v-select(label="Branch" :items="BranchChoices" v-model="branch"
            :rules="[v => !!v || 'Field is required']")
        center.my-5
          v-divider(width="90%")
        v-row.justify-center
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-phone" label="Phone Number" v-model="phone"
            :rules="[v => (!/[^0-9]/.test(v) && v.length==10) || !v || 'Enter a valid Number']")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-linkedin" label="Linkedin Profile LInk" v-model="linkedin"
            :rules="[v => /linkedin.com/.test(v) || !v || 'Enter a valid link', ]")
          v-col(cols=12 lg=4 sm=12)
            v-text-field( prepend-icon="mdi-github-circle" label="GitHub Profile LInk" v-model="github"
            :rules="[v => /github.com/.test(v) || !v || 'Enter a valid link', ]")
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
          v-btn.mr-5(:disabled ="!valid" color="success" @click="validate") Update
          v-btn.mr-5(color="red" @click="$router.push('/studentzone')") cancel
</template>
<script>
import { instance } from '@/api/axios'
import dfile from '@/assets/avad.png'
export default {
  name: 'CreateProfile',
  data: () => ({
    dfile,
    cfile: null,
    first_name: '',
    last_name: '',
    roll_number: '',
    year: '',
    prog: '',
    branch: '',
    gender: '',
    linkedin: '',
    github: '',
    file: null,
    phone: '',
    stack: [],
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
    var state = this.$store.state
    this.StackChoices = data.stack
    this.GenderChoices = data.gender
    this.BranchChoices = data.branch
    this.YearChoices = data.year
    this.ProgChoices = data.prog
    this.cfile = state.userProfile.avatar
    this.first_name = state.userProfile.user.first_name
    this.last_name = state.userProfile.user.last_name
    this.roll_number = state.userProfile.roll_number
    this.year = state.userProfile.year
    this.prog = state.userProfile.prog
    this.branch = state.userProfile.branch
    this.gender = state.userProfile.gender
    this.linkedin = state.userProfile.linkedin
    this.github = state.userProfile.github
    this.phone = state.userProfile.phone
    this.stack = state.userProfile.techstack
  },
  methods: {
    validate () {
      this.$refs.form.validate()
      var form = new FormData()
      try {
        form.append('avatar', this.file, this.file.name)
      } catch {}
      form.append('first_name', this.first_name)
      form.append('last_name', this.last_name)
      form.append('roll_number', this.roll_number)
      form.append('gender', this.gender)
      form.append('year', this.year)
      form.append('prog', this.prog)
      form.append('branch', this.branch)
      form.append('phone', this.phone)
      form.append('linkedin', this.linkedin)
      form.append('github', this.github)
      form.append('stack', this.stack)
      instance.post('/auth/profile-edit/', form)
        .then(res => {
          this.$store.state.userProfile = res.data
          window.location = '/studentzone'
        }).catch(err => console.log(err))
    },
    updatefile () {
      this.cfile = URL.createObjectURL(this.file)
    }
  }
}
</script>
