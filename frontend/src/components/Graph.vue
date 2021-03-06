<template>
<div>
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
          <div id="mynetwork"></div>
      </div>
</div>
</template>


<script lang="ts">


import {DataSet, Network} from 'vis-network/standalone'
import {Component, Vue} from 'vue-property-decorator'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components: {

    },
    props: ['patient']
})
export default class Graph extends Vue{
    patientName = this.$props.patient

    nodes = new DataSet([
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
        { id: 4, label: "Node 4" },
        { id: 5, label: "Node 5" },
    ])
    
    edges = [
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
        { from: 2, to: 5 },
        { from: 3, to: 3 },
    ]
    data = {nodes: this.nodes, edges: this.edges}
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
      },
      font: {
        color: 'white',
      },
    },
    edges: {
      width: 12,
      length: 175,
      selectionWidth: 14,
    },
    physics: {
      enabled: true,
      stabilization: {
        iterations: 1200,
      }
    },
    layout: {
      randomSeed: 2.5,
      improvedLayout: true,
    }
  }

  container: any = null
  network: any = null


  getMedicationFromEdge(edge: any){

    var from = ""
    var to = ""
    for(var i = 0; i < this.nodes.length; i++){
      if(this.nodes[i].id == edge.options.from){
        from = this.nodes[i].label
      }
      if(this.nodes[i].id == edge.options.to){
        to = this.nodes[i].label
      }
      var interaction = [from, to]
      this.$emit("childToParent", interaction)
    }
  }

  getMedicationFromNode(node: any){
    var med = ""
    for(var i = 0; i < this.nodes.length; i++){
      if(this.nodes[i].id == node.options.id){
        med = this.nodes[i].label
      }
    }
    this.$emit('nodeToParent', med)
  }
  mounted(){

    service.createGraph(this.patientName).then((response) =>{
      if(response.status = 200){
        this.nodes = response.data[0]
        this.edges = response.data[1]

        var netData = {nodes: this.nodes, edges: this.edges}
        //Hier De data inladen
        this.container = document.getElementById("mynetwork")
        this.network = new Network(this.container, netData, this.options)
        this.network.on('selectEdge', (params) =>{
          var edgeId = params.edges[0]
          var edge = this.network.body.edges[edgeId]
          this.getMedicationFromEdge(edge)
        })
        this.network.on('selectNode', (params) =>{
          var nodeId = params.nodes[0]
          var node = this.network.body.nodes[nodeId]
          this.getMedicationFromNode(node)
        })

        this.network.once('stabilized', () => {
          var scaleOption = { scale : 1.5}
          this.network.moveTo(scaleOption);
          this.network.fit()
        })
      }
    })
  }
}
</script>

<style scoped>

#mynetwork{
  height: 86%;
  width: 100%;
  margin: 5px 0;
}


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
    margin: 10px 25px 0px 0px;
  }
.wrapper{
  height: 575px;
  width: 100%;
  text-align: center;
  margin-top: 10px;
}


</style>