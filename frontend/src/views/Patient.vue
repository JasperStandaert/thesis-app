<template>
    <div id="patient" >
        <button @click="overview">Patients</button>
        <p>Hello {{patient.first_name}} {{patient.last_name}}</p>
        <v-container>
            <v-row>
                <v-col cols="6">
                    <medication-card :medication="patient.medication" :patient="patient"/>
                </v-col>
                <v-col cols="6">
                    <interaction-card :patient="name"/>
                </v-col>
            </v-row>
        </v-container>
        <div style="position: relative; width: 100%; height 500px;">
            <patient-graph :patient="name"/>
        </div>
    </div>
</template>
<script lang="ts">
import MedicationCard from '../components/MedicationCard.vue';
import InteractionCard from '../components/InteractionCard.vue';
import PatientGraph from '../components/PatientGraph.vue';
import router from "../router"
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {
        MedicationCard,
        InteractionCard,
        PatientGraph,
    },
    props: ['patient'],
})


export default class Patient extends Vue {
    patient: any =  this.$route.params.pat;
    name = this.patient.first_name + "_" + this.patient.last_name

    overview(){
        router.push("/")
    }
}
</script>

<style scoped>

</style>