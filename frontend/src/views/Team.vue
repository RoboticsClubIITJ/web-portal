<template>
  <div class="team mt-16">
    <v-container>
      <h1>OUR TEAM</h1>
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg4 v-for="member in members" :key="member.name">
          <v-card class="ma-5">
            <v-responsive>
              <v-img class="image" :src="member.member.avatar" alt="member.member.user.first_name"/>
            </v-responsive>
            <v-card-title class="name-desg">
              {{member.member.user.first_name}} {{member.member.user.last_name}} | {{member.position}}
            </v-card-title>
            <v-card-text style="overflow-y: auto; height:200px">
              <v-chip-group column>
                <v-chip color="green" outlined class="techstack" v-for="techstack in member.member.techstack" :key="techstack">{{techstack}}</v-chip>
              </v-chip-group>
            </v-card-text>
            <v-card-actions class="socials">
                <v-icon icon large color='red'>mdi-email</v-icon>
                <v-icon icon large color='black'>mdi-github-circle</v-icon>
                <v-icon icon large color='blue'>mdi-linkedin</v-icon>
            </v-card-actions>
            <div class="year">
              {{member.member.year}}
            </div>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { instance } from '../api/axios'
export default {
  name: 'Team',
  data () {
    return {
      members: []
    }
  },
  async created () {
    try {
      const res = await instance.get('/team')
      console.log(res.data)
      this.members = res.data
    } catch (e) {
      console.log(e)
    }
  }
}
</script>

<style>
  h1 {
    color: white;
    text-align: center;
  }
  .name-desg {
    justify-content: center;
    align-items: center;
  }
  .image {
    width: 100%;
    border-radius: 20px;
  }
  .socials {
    justify-content:space-evenly;
    align-items: center;
  }
  .year {
    background: grey;
    color: blue;
    text-align: center;
  }
</style>
