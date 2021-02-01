<script src="https://d3js.org/d3.v4.js"></script>
<template>
    <div id="patientGraph">
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
  patient = this.$props.patient
  nodes: any = []
  edges: any = []
  options: any = {
    nodes: {
    borderWidth: 4
    },
    edges: {
      color: 'lightgray'
    }
  }

  mounted(){
    service.createGraph(this.patient).then( (response) =>{
      if (response.status == 200){
      
        console.log(response.data)
      }
    }).catch((error) =>{
      console.log(error)
    });
  }
}
</script>
<style scoped>

</style>