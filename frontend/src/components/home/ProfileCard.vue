<template lang="pug">
  v-card.mx-auto.pa-7.p-card(style="border-radius:10%" max-width=300 elevation=16)
    center(:class="$vuetify.breakpoint.mobile ? 'd-flex' : ''")
      v-avatar(size=100)
        v-img(:src="member.member.avatar.pathname")
      v-spacer(v-if= "$vuetify.breakpoint.mobile")
      v-divider.ma-5(v-if= "!$vuetify.breakpoint.mobile")
      div.team-info
        h5 {{member.member.user.first_name}}&nbsp;{{member.member.user.last_name}}
        p {{member.position}}
        v-divider.ma-2
        div.d-flex.justify-center
          v-hover.mx-4(v-slot:default ="{ hover }" v-if="member.member.user.email")
            a(:href="'mailto:'+member.member.user.email" style="text-decoration: none;")
              v-icon(small :color ="hover?'#00d0ff':'#007bff'") mdi-gmail
          v-hover.mx-4(v-slot:default ="{ hover }" v-if="member.member.github")
            a(:href="member.member.github" style="text-decoration: none;")
              v-icon(small :color ="hover?'#00d0ff':'#007bff'") mdi-github-circle
          v-hover.mx-4(v-slot:default ="{ hover }" v-if="member.member.linkedin")
            a(:href="member.member.linkedin" style="text-decoration: none;")
              v-icon(small :color ="hover?'#00d0ff':'#007bff'") mdi-linkedin
</template>
<script>
export default {
  name: 'ProfileCard',
  props: {
    member: {
      type: Object,
      required: true
    }
  }
}
</script>
<style scoped>
.team-info h5{
    color: #7057f9;
    text-transform: uppercase;
    font-size: 18px;
    margin-bottom: 0px;
    line-height: 1.4;
    font-weight: 500;
  }
  .team-info p {
    color: #a592b4;
    text-transform: uppercase;
    font-size: 13px;
    margin-bottom: 0;
    line-height: 1.9;
  }
  .p-card{
  background: #ffffff; /* Old browsers */
  background: -moz-linear-gradient(-45deg, #ffffff 0%, #f3f3f3 50%, #ededed 51%, #ffffff 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(-45deg, #ffffff 0%,#f3f3f3 50%,#ededed 51%,#ffffff 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(135deg, #ffffff 0%,#f3f3f3 50%,#ededed 51%,#ffffff 100%);
  }
</style>
