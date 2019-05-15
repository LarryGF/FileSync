
<template>

<v-layout row>
  <v-flex xs6>

  <PathCard :light="false" direction="origen" :height="height" :key="0"/>
  </v-flex>
  <v-flex xs6>

  <PathCard :light="true" direction="destino" :height="height" :key="1"/>
  </v-flex>
  
  </v-layout>
</template>

<script>
import PathCard from '../components/PathCard'
export default {
  data () {
    return {
      height: 0
    }
  },
  watch: {
  },
  components: {
    PathCard
  },
  mounted () {
    // this.fetch()
    this.height = window.innerHeight * 0.7
  },
  methods: {

  }
}
</script>


