<template>
  <div class="mt-16 ml-6 mb-16 mr-6">
    <v-container class="text-center">
      <h1 class="header my-16">
        PROFILE <v-icon class="mb-1" x-large color='white'>mdi-account-circle</v-icon>
      </h1>
    </v-container>
    <v-container class="profile mt-16" :style="[$vuetify.breakpoint.mobile ? { 'width':'100%' } : { 'width':'70%' }]">
      <div class="text-center">
        <v-avatar class="elevation-10 my-14" size="180" style="margin-top: -110px !important;">
          <v-img :src="profile.avatar"></v-img>
        </v-avatar>
      </div>
      <div class="text-center">
        <h3><b>{{fullName}} ({{profile.roll_number}})</b></h3>
        <h5 class='text-muted mt-4 text-center' >{{profile.year}}</h5>
      </div>
      <v-row justify="center" class="mt-5">
        <v-col cols=12 lg=6 md=12 sm=12>
          <v-card
            shaped
            elevation="6"
            class="mx-auto"
          >
         <v-card-title class="headline justify-center">
            Personal Info
          </v-card-title>
          <v-divider class="mx-3 my-0"/>
          <v-card-text>
            <v-list disabled>
              <v-list-item-group>
                <v-list-item
                  v-for="(key, i) in Object.keys(iconList.socailInfo)"
                  :key="i"
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
            Skills
          </v-card-title>
          <v-divider class="mx-3 my-0"/>
          <v-card-text>
            <v-chip-group column>
                <v-chip medium color="#3C40C6" fill style="color: white" class="techstack" v-for="techstack in profile.techstack" :key="techstack">{{techstack}}</v-chip>
              </v-chip-group>
          </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data () {
    return {
      profile: []
    }
  },
  async created () {
    try {
      const userProfile = await this.$store.state.userProfile
      this.profile = userProfile
    } catch (e) {
      console.log(e)
    }
  },
  computed: {
    fullName: function () {
      return this.profile.user.first_name + ' ' + this.profile.user.last_name
    },
    iconList: () => ({
      socailInfo: {
        phone: { icon: 'mdi-phone', color: '#2ecc72' },
        email: { icon: 'mdi-email', color: '#FF3031' },
        linkedin: { icon: 'mdi-linkedin', color: '#0e76a8', linkIcon: 'mdi-link-variant' },
        github: { icon: 'mdi-github-circle', color: 'black', linkIcon: 'mdi-link-variant' }
      }
    })
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
