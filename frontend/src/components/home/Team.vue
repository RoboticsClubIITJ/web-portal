<template lang="pug">
    div.mt-16.container
      div.flex-column.h-100
        div(style="width:15%;margin:auto;")
          v-img(:src= "ShapeImg")
        div.d-flex.justify-center
          div.dream-dots(v-for= "color in DotColors" :class="color")
        div.h-text.pa-10 Our Awesome Team
        div.container
          v-row(v-if="pors.length")
            v-col.pa-5(
            cols=12 sm=12 md=4 lg=4
            v-for="member in pors" :key="member.id")
              ProfileCard(:member="member")
          v-row(v-if="webs.length")
            v-col.pa-5(
            cols=12 sm=12 md=3 lg=3
            v-for="member in webs" :key="member.id")
              ProfileCard(:member="member")
</template>
<script>
import ShapeImg from '@/assets/shape1.png'
import ProfileCard from '@/components/home/ProfileCard'
import { instance } from '@/api/axios'
export default {
  name: 'Team',
  components: {
    ProfileCard
  },
  data: () => ({
    ShapeImg,
    DotColors: ['red', 'green', 'blue', 'purple', 'orange', 'yellow'],
    pors: [],
    webs: []
  }),
  async created () {
    const resp = await instance.get('/team/homeview')
    var team = resp.data
    var cap = []
    var vcap = []
    team.forEach(element => {
      element.member.avatar = new URL(element.member.avatar)
      if (element.position === 'Captain') cap.push(element)
      else if (element.position === 'Vice-Captain') vcap.push(element)
      else this.webs.push(element)
      this.pors = [...cap, ...vcap]
    })
  }
}
</script>
<style scoped>
  .dream-dots{
    width: 8px;
    height: 8px;
    background-color: #fff;
    border-radius: 50%;
    margin-right: 5px;
  }
  .h-text{
    text-align: center;
    font-size: 30px;
    font-weight: 500;
    margin-bottom: 20px;
    color: #fff;
    line-height: 1.4;
  }
  .h-100{
    height: 100%;
    overflow: visible;
  }
</style>
