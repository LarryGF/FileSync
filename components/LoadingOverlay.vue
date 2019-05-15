<template>
  <v-container class="px-0 py-0" text-xs-center :style="'height:'+height+'px' +';position:absolute'">

    <v-card height="100%" width="100%" flat color="transparent" text-xs-center>
      <v-container fill-height>
        <v-layout column justify-center align-center>
          <v-progress-circular :size="70" :width="7" color="primary" indeterminate></v-progress-circular>
        </v-layout>
      </v-container>
    </v-card>
  </v-container>
</template>
<script>
export default {
    props:{
        height:Number
    }
}
</script>

