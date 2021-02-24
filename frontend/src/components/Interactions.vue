<template>
        <vs-card>
        <v-container>
            <v-row>
                <v-col cols="7">
                    <h1>Interaction Graph</h1>
                    <p> Active interaction: {{activeInteraction}}</p>
                    <graph :patient="name" v-on:childToParent="clickedInteraction"/> 
                </v-col>
                <v-col cols="5">
                    <vs-card outlined class="interactionCard">
                        <v-card-title class="title">
                            Interactions
                        </v-card-title>
                        <interaction-info v-for="(inter, i) in interactions" :key="i+1" :drugA="inter[0]" :drugB="inter[1]" :active="activeInteraction"/>
                    </vs-card>
                </v-col>
            </v-row>
        </v-container>
        </vs-card>
</template>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import Graph from '../components/Graph.vue'
import InteractionInfo from '../components/InteractionInfo.vue'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components: {
        Graph,
        InteractionInfo,
    },
    props: ['patient']

})
export default class Interactions extends Vue{
    patient = this.$props.patient
    name = this.patient.first_name + "_" + this.patient.last_name
    interactions: any = []

    activeInteraction = ['','']

    
    mounted(){

        service.getInteractions(this.name).then((response) =>{
            if(response.status == 200){
                this.interactions = response.data
            }
        }).catch((error) =>{
            console.log(error)
        })
    }

    clickedInteraction(interaction){
        this.activeInteraction = interaction
    }
    
}
</script>