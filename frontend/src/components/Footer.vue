<template>
  <div class="flex-column" style="margin-top:3%">
    <div class="row indigo" style="margin:0">
      <v-card
        class="indigo white--text col-md-12 mar"
        flat
        tile
        fluid
      >
        <v-card-title class="justify-center">
          <v-btn
            v-for="(icon, idx) in icons"
            :key="idx"
            class="mx-3"
            dark
            icon
          >
            <a class="white--text text-decoration-none" :href="icon.url"><v-icon size="25px">{{ icon.name }}</v-icon></a>
          </v-btn>
        </v-card-title>
        <div class="col-md-4 fl indigo ">
          <p class="head"><a href="https://www.google.com/maps/place/Indian+Institute+of+Technology+Jodhpur/@26.4711759,73.1120891,17.47z/data=!4m12!1m6!3m5!1s0x39418c5ea672337b:0xb6c9a5a9b08db22e!2sIndian+Institute+of+Technology+Jodhpur!8m2!3d26.4710809!4d73.1134335!3m4!1s0x39418c5ea672337b:0xb6c9a5a9b08db22e!8m2!3d26.4710809!4d73.1134335" class="text-decoration-none white--text">
            <span class="mdi mdi-map-marker white--text" style="padding:1%"></span>INDIAN INSTITUTE OF TECHNOLOGY, JODHPUR</a>
          </p>
          <p class="add">NH-65, Surpura Bypass Road</p>
          <p class="add">Karwar, Rajasthan 342037</p>
        </div>
        <div class="col-md-4 fl indigo">
          <v-img src="../assets/robologo.svg"></v-img>
        </div>
        <div class="col-md-4 fl indigo">
        <p class="head1">QUICK LINKS</p>
        <p class="add1"><a class="white--text text-decoration-none" href="http://iitj.ac.in/">IIT Jodhpur</a></p>
        <p class="add1"><a class="white--text text-decoration-none" href="https://students.iitj.ac.in/">IITJ Gymkhana</a></p>
        </div>
      </v-card>
    </div>
    <v-footer
      dark
      height=auto
      class="flex:1 pad indigo darken-1 white--text text-center justify-center">
      <v-card
        class="flex:1 indigo darken-1 white--text col-md-12"
        flat
        tile
        fluid
      >
      <div class=" pad col-sm-12 col-md-12">
        <h6 class="pad text-center">&copy;2020 COPYRIGHT <span style="padding:1%">|</span><br v-if="$vuetify.breakpoint.mobile">
          Made with<span class="mdi mdi-heart red--text" style="padding:3px"></span>by Robotics WebD Team
        </h6>
      </div>
      </v-card>
    </v-footer>
  </div>
</template>
<style scoped>
    .head{
        padding: 0px;
        margin-top:0px;
        text-align: center;
        font-weight: 500;
        font-size: 20px;
    }
    .head1{
        padding: 0px;
        margin-top:0px;
        text-align: center;
        font-weight: 500;
        font-size: 20px;
    }
    .add{
        padding-top: 0px;
        margin-top: 0px;
        text-align: center;
        font-size: 17px;
        font-weight: 300;
    }
    .add1{
        padding-top: 0px;
        margin-top: 0px;
        text-align: center;
        font-size: 17px;
        font-weight: 300;
    }
    .fl{
        float:left;
    }
    .mar{
        margin:0px;
        padding:0px;
        border:none
    }
    .pad{
        padding:0px;
        margin:0px;
        font-weight:400;
        border:none
    }
</style>
<script>
export default {
  data: () => ({
    icons: [
      {
        name: 'mdi-gmail',
        url: 'mailto:robotics@iitj.ac.in'
      },
      {
        name: 'mdi-github-circle',
        url: 'https://github.com/RoboticsClubIITJ'
      },
      {
        name: 'mdi-facebook',
        url: 'https://www.facebook.com/robotics.iitj/'
      },
      {
        name: 'mdi-linkedin',
        url: 'https://www.linkedin.com/company/robotics-club-iit-jodhpur/'
      },
      {
        name: 'mdi-instagram',
        url: 'https://www.instagram.com/roboticsiitj/?hl=en'
      }
    ]
  })
}

</script>
