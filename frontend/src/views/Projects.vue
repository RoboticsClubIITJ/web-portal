<template>
  <v-container>
  <h1 class="header mt-16">PROJECTS</h1>
  <v-layout row wrap>
  <v-flex xs12 sm6 md4 lg4 v-for="project in projects"
    :key="project.name">
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
    <v-card-title v-text="project.name">
    </v-card-title>

    <v-card-subtitle v-text="project.status">
    </v-card-subtitle>
    <v-card-actions class="mar2">
    <v-btn dark color="blue" absolute right small fab v-if="project.repository_link!=null">
        <a class="white--text text-decoration-none" :href="project.repository_link"><v-icon>mdi-github-circle</v-icon></a>
    </v-btn>
    <v-btn dark color="pink" absolute small fab v-if="project.project_url!=null">
        <a class="white--text text-decoration-none" :href="project.project_url"><v-icon>mdi-web</v-icon></a>
    </v-btn>
    </v-card-actions>
    <div style="height:120px">
    <v-chip
        v-for="(member, idx1) in project.members"
        :key="idx1"
        class="ma-2"
        small
        color="deep-purple accent-4"
        outlined
      >{{ member }}
    </v-chip>
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
  name: 'Projects',
  data () {
    return {
      projects: [],
      members: []
    }
  },
  async created () {
    try {
      const res = await instance.get('projects/project-list')
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
