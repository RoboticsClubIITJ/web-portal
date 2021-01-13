<template>
<div>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <v-card :loading="loader">
        <v-card-title>
          <span class="headline">Register For {{comp.title}}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                 :error-messages="err_m1"
                  label="Code/Name*"
                  v-model="code_f"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*Enter Team to Join a team or A name to Create a new team</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
          class="pa-5"
            color="primary"
            @click="create"
          >
            Create
          </v-btn>
          <v-btn
          class="pa-5"
            color="success"
            @click="join"
          >
            Join
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="$router.push('/competitions')"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
  <div class="mt-16 ml-6 mb-16 mr-6">
    <v-container class="text-center">
      <h1 class="header my-16">
        {{comp.title}} <v-icon class="mb-1" x-large color='white'>mdi-book</v-icon>
      </h1>
    </v-container>
    <v-container  v-if="registered" class="profile" :style="[$vuetify.breakpoint.mobile ? { 'width':'100%' } : { 'width':'70%' }]">
      <div class="text-center">
        <h3><b>{{team.name}} ( {{team.code}} ) </b></h3>
      </div>
      <v-row justify="center" class="mt-5">
        <v-col cols=12 lg=6 md=12 sm=12>
          <v-card
            shaped
            elevation="6"
            class="mx-auto"
          >
         <v-card-title class="headline justify-center">
            Submissions
          </v-card-title>
          <v-divider class="mx-3 my-0"/>
          <v-card-text>
            <v-list disabled>
              <v-list-item-group>
                <v-list-item
                  v-for="i in comp.submissions"
                  :key="i.id"
                >
                  <v-list-item-icon>
                    <v-icon  v-if="key === 'email'" medium :color=iconList.socailInfo[key].color>{{ iconList.socailInfo[key].icon }}</v-icon>
                    <v-icon v-else medium :color=iconList.socailInfo[key].color>{{ iconList.socailInfo[key].icon }}</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title v-if="key === 'email'">{{ profile.user[key] }}</v-list-item-title>
                    <v-list-item-title v-else>{{ profile[key] }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
          </v-card>
        </v-col>
        <v-col cols=12 lg=6 md=12 sm=12>
          <v-card
            shaped
            elevation="6"
            class="mx-auto"
          >
          <v-card-title class="headline justify-center">
            Members
          </v-card-title>
          <v-divider class="mx-3 my-0"/>
          <v-card-text>
            <v-chip-group row>
                <v-chip medium color="#3C40C6" fill style="color: white" class="techstack" v-for="pi in team.members" :key="pi.email">{{pi.first_name}} ( {{pi.email}} )</v-chip>
              </v-chip-group>
          </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
  <div v-if="dialog" style="height: 500px"></div>
</div>
</template>

<script>
import { instance } from '../api/axios'
export default {
  name: 'CompCard',
  data () {
    return {
      code_f: '',
      err_m1: '',
      loader: false,
      comp: null,
      team: null,
      registered: false,
      dialog: true,
      profile: [],
      id: this.$route.params.id
    }
  },
  async created () {
    try {
      const userProfile = this.$store.state.userProfile
      this.profile = userProfile
      const res = await instance.post('competitions/register/', { id: this.$route.params.id })
      if (res.data.registered) {
        this.team = res.data.team
      }
      this.comp = res.data.comp
      this.registered = res.data.registered
      this.dialog = !this.registered
      console.log(res.data)
    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async join () {
      this.loader = true
      const res = await instance.post('competitions/register/', { id: this.$route.params.id, code: this.code_f })
      if (res.data.registered) {
        this.comp = res.data.comp
        this.team = res.data.team
        this.registered = res.data.registered
        this.dialog = !this.registered
      } else {
        this.err_m1 = res.data.data
      }
    },
    async create () {
      this.loader = true
      const res = await instance.post('competitions/register/', { id: this.$route.params.id, team_name: this.code_f })
      console.log(res.data)
      if (res.data.registered) {
        this.comp = res.data.comp
        this.team = res.data.team
        this.registered = res.data.registered
        this.dialog = !this.registered
      } else {
        this.err_m1 = res.data.data
      }
    }
  }
}
</script>

<style>
.profile{
  border-top-left-radius: 24px;
  border-top-right-radius: 4px !important;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 24px;
  background: white;
}
.editButton{
  pointer-events: none;
  opacity: 0.7;
}
</style>
