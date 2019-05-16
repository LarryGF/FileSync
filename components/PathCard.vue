<template>
  <v-layout class="mx-2" column align-center fill-height>
    <v-card height="100%" width="100%" :light="light">
      <v-card-title>
        <v-btn fab color="pink" class="mb-4" @click.stop.prevent="goBack">
          <v-icon color="white" >arrow_back</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <h2 class="mb-4 mx-2">{{direction.toUpperCase()}}:</h2>
        <v-flex xs7>
          <v-text-field
            outline
            v-model="Route"
            append-icon="send"
            :label="'Copie la ruta ' +direction"
            @click:append="progressivePath=[Route], getRoute()"
            @keyup.enter.native.stop="progressivePath=[Route] ,getRoute()"
          ></v-text-field>
        </v-flex>
        <v-spacer></v-spacer>
      </v-card-title>

      <v-container
        class="scroll-y py-0 px-0"
        :style="'height:'+height+'px'"
        v-if="origin.length!=0"
      >
        <LoadingOverlay v-if="loading" :height="height"/>

        <v-treeview
          hoverable
          :active.sync="active"
          :items="origin"
          :open.sync="open"
          activatable
          active-class="primary--text"
          transition
        >
          <v-icon
            v-if="item.children"
            slot="prepend"
            slot-scope="{ item, active }"
            :color="active ? 'primary' : ''"
          >folder</v-icon>
          <v-icon
            v-else
            slot="prepend"
            slot-scope="{ item, active }"
            :color="active ? 'primary' : ''"
          >assignment</v-icon>
        </v-treeview>
      </v-container>


      <v-container v-else :style="'height:'+height+'px'"></v-container>

      <v-card-actions   v-if="direction=='destino'" class="pt-3">
        <v-radio-group top v-model="type" row color="purple" height="10" class="mt-3">
      <v-radio label="Series" value="seriePersona"></v-radio>
      <v-radio label="Animes" value="anime"></v-radio>
      <v-radio label="Películas" value="pelicula"></v-radio>
    </v-radio-group>
        <v-spacer></v-spacer>
        <v-btn color="primary"  @click="organize">Organizar</v-btn>
      </v-card-actions>

    </v-card>
  </v-layout>
</template>



<script>
import LoadingOverlay from "../components/LoadingOverlay";
export default {
  name: "PathCard",
  props: {
    light: Boolean,
    direction: String,
    height: Number,
    value: String
  },
  data() {
    return {
      type:'seriePersona',
      test:0,
      loading: false,
      open: [],
      progressivePath: [],
      Route: "",
      active: [],
      origin: []
    };
  },
  methods: {
    intoFolder: async function(item) {
      // eslint-disable-next-line no-undef,no-return-assign
      // eel.into_folder(String(item), this.Route)((result) => { this.origin = result['items']; this.Route = result['route']; this.progressivePath.push(this.Route) })
      var result = await this.$axios.post(
        "http://localhost:8000/into_folder/",
        {
          item: String(item),
          route: this.Route
        }
      );
      this.origin = result.data.items;
      this.Route = result.data.route;
      this.$emit('change', this.Route)
      this.$emit('input', this.Route)
      this.progressivePath.push(this.Route);
    },
    getRoute: async function() {
      //   this.progressivePath.push(this.Route)
      this.$emit('change', this.Route)
      this.$emit('input', this.Route)
      this.origin = (await this.$axios.post(
        "http://localhost:8000/get_route/",
        {
          name: this.Route
        }
      )).data;
    },
    goBack: function() {
      this.$emit('change', this.Route)
      this.$emit('input', this.Route)
      console.log('going back')
      if (this.progressivePath.length > 1) {
        this.progressivePath.pop();
        this.active.pop()
        this.Route = this.progressivePath[this.progressivePath.length - 1];
        this.getRoute();
        this.$forceUpdate();
      }
    },
    organize: async function(){
      this.loading = true
      var result = (await this.$axios.post("http://localhost:8000/organize/",{
        route:this.Route,
        type:this.type
      })).data
      this.loading = false
      this.getRoute()
      console.log(result)
    },
    
  },
  watch: {
    active: function() {
      if (this.active.length !== 0) {
        this.intoFolder(this.active[0]);
      }
    }
  },
  components: {
    LoadingOverlay
  }
};
</script>
