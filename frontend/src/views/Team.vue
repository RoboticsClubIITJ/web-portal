<template>
  <div class="team mt-16">
    <v-container>
      <h1 class="header mt-16">OUR TEAM</h1>
      <v-text-field
        dense
        dark
        rounded
        filled
        label="Search by name or skill"
        prepend-icon="mdi-magnify"
        color="white" class="mt-16 mb-16"
        v-on:input="searchMember">
      </v-text-field>
      <h1 class="noResult ma-16" v-if="members.length == 0">
        There are no results :(
      </h1>
      <v-layout row wrap v-else>
        <v-flex xs12 sm6 md4 lg4 v-for="member in members" :key="member.name">
          <mdb-card class="ma-5 member-card" style="border-radius:25px">
            <v-img src="@/assets/member-bg4.jpg" height="140" width="100%" style="border-top-left-radius: 25px; border-top-right-radius: 25px;"></v-img>
            <mdb-card-body class="text-center pb-0" cascade>
              <v-avatar class="ma-2" size="140" style="margin-top: -90px !important; border: 5px white solid">
                <v-img :src="member.member.avatar.pathname"></v-img>
              </v-avatar>
              <mdb-card-title><strong>{{member.member.user.first_name}} {{member.member.user.last_name}}</strong></mdb-card-title>
              <h5 style="color:#4A148C"><strong>{{member.position}}</strong></h5>
              <mdb-card-text style="height:150px">
                <v-chip-group column>
                  <v-chip small color="#4A148C" fill dark class="techstack" v-for="techstack in member.member.techstack" :key="techstack">{{techstack}}</v-chip>
                </v-chip-group>
              </mdb-card-text>
              <v-card-actions class="socials">
                <v-btn text icon medium color='#FF3031' :href="`mailto:${member.member.user.email}`" target="_blank">
                  <v-icon medium color='#FF3031'>mdi-email</v-icon>
                </v-btn>
                <v-btn text icon medium color='black' :href="member.member.github" target="_blank">
                  <v-icon icon medium color='black'>mdi-github-circle</v-icon>
                </v-btn>
                <v-btn text icon medium color='#0e76a8' :href="member.member.linkedin" target="_blank">
                  <v-icon medium color='#0e76a8'>mdi-linkedin</v-icon>
                </v-btn>
              </v-card-actions>
            </mdb-card-body>
            <mdb-card-footer class="text-muted mt-4 text-center">{{member.member.year}}</mdb-card-footer>
          </mdb-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { instance } from '../api/axios'
import { mdbCard, mdbCardTitle, mdbCardText, mdbCardFooter, mdbCardBody } from 'mdbvue'
export default {
  name: 'Team',
  components: {
    mdbCard,
    mdbCardTitle,
    mdbCardText,
    mdbCardFooter,
    mdbCardBody
  },
  data () {
    return {
      members: []
    }
  },
  async created () {
    try {
      const res = await instance.get('/team')
      this.members = res.data
      this.members.forEach(member => {
        member.member.avatar = new URL(member.member.avatar)
        member.member.github = new URL(member.member.github)
        member.member.linkedin = new URL(member.member.linkedin)
      })
    } catch (e) {
      console.log(e)
    }
  },
  methods: {
    async searchMember (searchData) {
      try {
        const res = await instance.get(`/team?search=${searchData}`)
        this.members = res.data
        this.members.forEach(member => {
          member.member.avatar = new URL(member.member.avatar)
          member.member.github = new URL(member.member.github)
          member.member.linkedin = new URL(member.member.linkedin)
        })
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style>
  .header {
    color: white;
    text-align: center;
    font-weight: 400;
  }
  .noResult {
    color: white;
    text-align: center;
    font-weight: 400;
  }
  .socials {
    justify-content:space-evenly;
    align-items: center;
  }
</style>
