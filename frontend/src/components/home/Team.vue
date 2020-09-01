<template lang="pug">
    div.mt-16.container
      div.flex-column.h-100
        div(style="width:15%;margin:auto;")
          v-img(:src= "ShapeImg")
        div.d-flex.justify-center
          div.dream-dots(v-for= "color in DotColors" :class="color")
        div.welcome-text.pa-10 Our Awesome Team
</template>
<script>
import ShapeImg from '@/assets/shape1.png'
export default {
  name: 'Team',
  data: () => ({
    ShapeImg,
    DotColors: ['red', 'green', 'blue', 'purple', 'orange', 'yellow']
  })
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
  .welcome-text{
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
