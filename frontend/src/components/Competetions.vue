<template>
  <v-main class="h-100 transparent">
    <carousel-3d :width="500" :height="633" class="mt-10">
      <slide v-for="(item, i) in items" :index="i" :key="i">
        <v-card>
          <v-img src="https://cdn.vuetifyjs.com/images/cards/cooking.png"></v-img>
          <v-card-title>{{ item.name }}</v-card-title>
          <v-card-text><div>{{ item.description }}</div></v-card-text>
          <v-divider class="mx-4"></v-divider>
          <v-card-title>Starting on</v-card-title>
          <v-card-text column><v-chip>August 5th 2021</v-chip></v-card-text>
              <v-card-actions>
                <v-btn
                  color="deep-purple lighten-2"
                  text
                  @click="register"
                >
                  Register
                </v-btn>
              </v-card-actions>
        </v-card>
      </slide>
    </carousel-3d>
  </v-main>
</template>
<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
export default {
  name: 'Competetions',
  data () {
    return {
      items: [
        { name: 'Competetion 1', description: 'Description 11111' },
        { name: 'Competetion 2', description: 'Description 22222' },
        { name: 'Competetion 3', description: 'Description 33333' },
        { name: 'Competetion 4', description: 'Description 44444' },
        { name: 'Competetion 5', description: 'Description 55555' },
        { name: 'Competetion 6', description: 'Description 66666' },
        { name: 'Competetion 7', description: 'Description 77777' },
        { name: 'Competetion 8', description: 'Description 88888' },
        { name: 'Competetion 9', description: 'Description 99999' },
        { name: 'Competetion 10', description: 'Description 1010101010' }
      ]
    }
  },
  components: {
    Carousel3d,
    Slide
  }
}
</script>
<style scoped>
</style>
