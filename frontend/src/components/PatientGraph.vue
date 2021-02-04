<template>
  <vs-card>
    <v-card-title>
      Medical information visualized
    </v-card-title>
    <v-card-text>
    </v-card-text>
    <div class="container">
      <network :nodes="nodes" :edges="edges" :options="options"></network>
    </div>
  </vs-card>
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

.container{
  display: flex;
  padding: 10px;
  height: 300px;
}

</style>