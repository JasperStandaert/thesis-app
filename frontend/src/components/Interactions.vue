<template>
    <v-container>
            <v-row>
                <v-col cols="7">
                    <vs-card>
                        <v-card-title>Interaction Graph</v-card-title>
                        <v-card-content>
                            <graph/>
                        </v-card-content>
                    </vs-card>
                </v-col>
                <v-col cols="5">
                    <vs-card outlined class="interactionCard">
                        <v-card-title class="title">
                        Interactions
                        </v-card-title>
                        <v-card-content>
                            <interaction-info v-for="(inter, i) in interactions" :key="i+1" :drugA="inter[0]" :drugB="inter[1]"/>
                        </v-card-content>
                </vs-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import Graph from '../components/Graph.vue'
import InteractionInfo from '../components/InteractionInfo.vue'
import HttpService from '../service'
import store from '../store'

const service = new HttpService();

@Component({
    components: {
        Graph,
        InteractionInfo,
    },

})
export default class Interactions extends Vue{
    patient = store.getters.patient
    interactions: any = []
    
    mounted(){
        var name = store.state.patient.first_name + '_' + store.state.patient.last_name
        service.getInteractions(name).then((response) =>{
            if(response.status == 200){
                this.interactions = response.data
                store.commit('addInteractions', response.data)
            }
        }).catch((error) =>{
            console.log(error)
        })
    }
}
</script>

<style scoped>
v-container{
    margin-top: 200px;
}

</style>