<template>
    <v-container>
            <v-row>
                <v-col cols="7">
                    <vs-card>
                        <v-card-title>Interaction Graph</v-card-title>
                        <v-card-content>
                            <graph :patient="name" v-on:childToParent="clickedInteraction"/>
                        </v-card-content>
                    </vs-card>
                </v-col>
                <v-col cols="5">
                    <vs-card outlined class="interactionCard">
                        <v-card-title class="title">
                        Interactions
                        </v-card-title>
                        <v-card-content>
                            <interaction-info v-for="(inter, i) in interactions" :key="i+1" :drugA="inter[0]" :drugB="inter[1]" :active="activeInteraction"/>
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

<style scoped>

</style>