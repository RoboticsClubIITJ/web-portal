<template>
  <div class="team">
    <h1>This is team page</h1>
    <ul>
      <li v-for="member in members" :key="member.id">{{member.member.name}}</li>
      <v-img v-for="member in members" :key="member.member.name" :src="member.member.avatar" aspect-ratio="1.7"/>
    </ul>
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
