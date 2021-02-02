<template>
  <div id="patientGraph" style="position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px;">
    <network ref="network" :nodes="nodes" :edges="edges" :options="options"></network>
  </div> 
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
    nodes: {
    borderWidth: 1,
    },
    edges: {
      width: 10,
      selectionWidth: 14,
      length: 200
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
}
</script>
<style scoped>

</style>