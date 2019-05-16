
<template>

<v-layout row>
  {{error}}
  <v-flex xs6>
  <PathCard :light="false" direction="origen" :height="height" :key="0" v-model="source"/>
  </v-flex>
  <v-flex xs6>

  <PathCard :light="true" direction="destino" :height="height" :key="1" v-model="destination"/>
  </v-flex>
  <v-btn color="pink" :disabled="checkDisabled()" round absolute bottom class="mb-5" @click="move">Mover</v-btn>
  <v-dialog
      v-model="dialog"
      persistent
      width="300"
    >
      <v-card
        color="primary"
        dark
      >
        <v-card-text>
          Moviendo los archivos
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import PathCard from '../components/PathCard'
import LoadingOverlay from '../components/LoadingOverlay'
export default {
  data () {
    return {
      height: 0,
      source: '',
      destination:'',
      dialog:false.dialog,
      error:''
    }
  },
  watch: {
  },
  components: {
    PathCard,
    LoadingOverlay
  },
  mounted () {
    // this.fetch()
    this.height = window.innerHeight * 0.7
  },
  methods: {
    checkDisabled: function(){
      if(this.source ==='' || this.destination ===''){
        return true
      } else{
        return false
      }
    },
    move: async function(){
      this.dialog=true
      var result = (await this.$axios.post('http://localhost:8000/move/',{
        source:this.source,
        destination:this.destination,
        type: 'seriePersona'
      })).data
      if (result == true){
        this.dialog = false

      }else{
        this.dialog = false
        this.error = result
      }

    }
  },
  watch:{

  }
}
</script>


