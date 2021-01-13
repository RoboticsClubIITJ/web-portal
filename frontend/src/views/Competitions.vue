<template>
  <v-container>
  <h1 class="header mt-16">Competitions</h1>
  <v-layout row wrap>
  <v-flex xs12 sm6 md4 lg4 v-for="project in projects"
    :key="project.title">
  <v-card
    :elevation="10"
    md3
    style="border-radius:30px"
    class="mx-auto cardstyle"
  >
    <v-img
      :src="project.img_tile"
      height="200px"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      style="margin-bottom:10px;"
    >
    </v-img>
    <v-card-title v-text="project.title">
    </v-card-title>
    <v-card-subtitle>
        Starts on {{project.start}}
    </v-card-subtitle>
    <v-chip color="deep-purple accent-4"
        outlined v-text="project.status" class="ma-2">
    </v-chip>
    <v-card-actions class="mar2">
    <v-btn dark color="blue" absolute right v-if="project.registration_active">
        <a class="white--text text-decoration-none" :href="`/studentzone/competitions/${project.id}`">Register</a>
    </v-btn>
    <v-btn dark color="pink" absolute m v-if="project.rule_book!=null">
        <a class="white--text text-decoration-none" :href="project.rule_book"><v-icon>mdi-book</v-icon> Rules</a>
    </v-btn>
    </v-card-actions>
    <div style="height:60px">
    <v-chip
        v-for="(member, idx1) in project.members"
        :key="idx1"
        class="ma-2"
        small
        color="deep-purple accent-4"
        outlined
      >{{ member }}
    </v-chip>
    <div class="ma-4">
        <div v-for="a in project.announcement" :key="a">
            {{ a }}
        </div>
    </div>
    </div>
    <v-expansion-panels flat>
      <v-expansion-panel>
        <v-expansion-panel-header class="details">
          Details
          <template v-slot:actions>
            <v-icon color="pink">$expand</v-icon>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          {{project.description}}
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
  </v-flex>
  </v-layout>
  </v-container>
</template>
<script>
import { instance } from '../api/axios'
export default {
  name: 'Competitions',
  data () {
    return {
      projects: [],
      members: []
    }
  },
  async created () {
    try {
      const res = await instance.get('competitions/get')
      this.projects = res.data
    } catch (e) {
      console.log(e)
    }
  }
}
</script>

<style>
/* global scope for override v-btn styles */
button.v-btn, button.v-expansion-panel-header {
  outline: none;
}
</style>

<style scoped>
.header {
    color: white;
    text-align: center;
    font-weight: 400;
  }
.cardstyle{
    margin-top:60px;
    width: 320px;
    background-image: linear-gradient(45deg, #edeaeb 25%, #ffffff 25%, #ffffff 50%, #edeaeb 50%, #edeaeb 75%, #ffffff 75%, #ffffff 100%);
}
.mar{
  margin-left: 20px;
  margin-right: 20px;
}
.details{
  font-weight:500;
  outline: none;
}
.mar2{
  margin-bottom: 20px;
  margin-top: 20px;
}
</style>
