<template>
  <vs-card>
    <v-card-title>
      Interaction Graph
    </v-card-title>
    <v-card-content>
      <div class="wrapper">
        <network
          class="network"
          ref="network"
          :edges="edges"
          :nodes="nodes"
          :options="options"
          @select-edge="selectedInteraction()">
        </network>
      </div>
    </v-card-content>
  </vs-card>
<!--
  <vs-card class="patientGraph">
    <v-card-title>
      Medical information visualized
    </v-card-title>
    <v-card-text>
    </v-card-text>
    <div class="container">
      <network class="network" ref="network" :nodes="nodes" :edges="edges" :options="options" @select-edge="selectedInteraction()"></network>
    </div>
  </vs-card>
-->

</template>


<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service'
const service = new HttpService();
@Component({
    components: {
    },
    props: ['patient']
})

export default class PatientGraph extends Vue {
  patientName = this.$props.patient


  selected: any = null
  nodes: any = []
  edges: any = []
    options: any = {
      autoResize: true,
    nodes: {
      borderWidth: 2,
      size: 24,
      color: {
        border: 'grey',
        highlight: {
          border: 'black',
          background: '#2e6dff',
        },
        hover: {
          border: 'orange',
          background: 'grey',
        }
      },
      font: {
        size: 16,
        color: '#ffffff'
      }
    },
    edges: {
      width: 8,
      selectionWidth: 10,
      length: 200,
    },
    physics: {
      enabled: true,
      stabilization: {
        iterations: 5,    
      },
    },
    layout: {
      randomSeed: 2.554,
    }
  }

  mounted(){
    service.createGraph(this.patientName).then( (response) =>{
      if (response.status == 200){
        this.nodes = response.data[0]
        this.edges = response.data[1]
      }
    }).catch((error) =>{
      console.log(error)
    });
  }

  selectedInteraction(edge: any){
    console.log("Edge selected: " + edge.from)
  }
}
</script>
<style scoped>

.wrapper{
  padding: 20px 50px;
  text-align: center;
}

.container{
  padding: 20px 50px;
  text-align: center;
}

.network{
  height: 450px;
  border: 2px solid #ccc;
  border-radius: 20px;
  margin: 5px 0;
}

.patientGraph{
  height: 500px;
}

</style>