<template>
  <vs-card>
    <v-card-title>
      Interaction Graph
    </v-card-title>

    <v-card-content>
      
      <div class="my-legend">
        <div class="legend-title">Interaction colors</div>
        <div class="legend-scale">
          <ul class="legend-labels">
            <li><span style="background: #ffdd00"></span>Noticeable</li>
            <li><span style="background: #ff9d0a"></span>Mild</li>
            <li><span style="background: #ff2600"></span>Severe</li>
          </ul>
        </div>
      </div>
      <div class="wrapper">
        <network
          class="network"
          ref="network"
          :nodes="network.nodes"
          :edges="network.edges"
          :options="options"
          @select-edge="test()">
        </network>
      </div>
    </v-card-content>
  </vs-card>
</template>


<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();
@Component({
    components: {
    },
    props: ['patient']
})

export default class PatientGraph extends Vue {

  patientName = this.$props.patient

  nodes: any = []
  edges: any = []

  network: any = {
    nodes: this.nodes,
    edges: this.edges,
  }

  options={
    autoResize: true,
    width: '100%',
    height: '100%',
    nodes:{
      shape: 'circle',
      color: {
        border: 'darkgrey',
        background: '#2e5cff',
        highlight: {
          background: '#2e6dff'
        },
      }
    },
    edges: {
      width: 10,
      length: 175,
    },
    physics: {
      enabled: true,
      stabilization: {
        iterations: 1200,
      }
    },
    layout: {
      randomSeed: 2.554,
      improvedLayout: true,
    }
  }

  test(){
    console.log("You clicked on a link!")
  }
   

  mounted(){
    service.createGraph(this.patientName).then( (response) =>{
      if (response.status == 200){
        this.nodes = response.data[0]
        this.edges = response.data[1]
      }
      for(var i = 0; i < this.nodes.length; i++){
        this.network.nodes.push(this.nodes[i])
      }
      for(var i = 0; i < this.edges.length; i++){
        this.network.edges.push(this.edges[i])
      }
    }).catch((error) =>{
      console.log(error)
    });
  }
}
</script>
<style scoped>
.my-legend .legend-title {
    text-align: left;
    margin-bottom: 8px;
    font-weight: bold;
    font-size: 90%;
    }
  .my-legend .legend-scale ul {
    margin: 0;
    padding: 0;
    float: left;
    list-style: none;
    }
  .my-legend .legend-scale ul li {
    display: block;
    float: left;
    width: 50px;
    margin-bottom: 6px;
    text-align: center;
    font-size: 80%;
    list-style: none;
    }
  .my-legend ul.legend-labels li span {
    display: block;
    float: left;
    height: 15px;
    width: 50px;
    }
  .my-legend{
    display: block;
    float: right;
    margin: -46px 12px 0px 0px;
  }
.wrapper{
  height: 620px;
  width: 100%;
  text-align: center;
}

.network{
  height: 100%;
  width: 100%;
  margin: 5px 0;
}

.patientGraph{
  height: 500px;
}

</style>