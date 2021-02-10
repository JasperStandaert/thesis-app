<template>
    <div id="patient" >
        <profile-header :fn='patient.first_name' :ln='patient.last_name'/>
        <v-container>
            <v-row>
                <v-col cols="6">
                    <patient-card :patient="patient"/>
                </v-col>
                <v-col cols="6">
                    <medication-card :medication="patient.medication" :patient="patient"/>
                </v-col>
            </v-row>
        </v-container>
        <button @click='seeGraph()'>Click to see graph</button>
    </div>
</template>
<script lang="ts">
import MedicationCard from '../components/MedicationCard.vue';
import ProfileHeader from '../components/ProfileHeader.vue'
import InteractionCard from '../components/InteractionCard.vue';
import PatientGraph from '../components/PatientGraph.vue';
import PatientCard from '../components/PatientCard.vue'
import router from "../router"
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {
        MedicationCard,
        InteractionCard,
        PatientCard,
        PatientGraph,
        ProfileHeader,
    },
    props: ['patient'],
})


export default class Patient extends Vue {
    patient: any =  this.$route.params.pat;
    name = this.patient.first_name + "_" + this.patient.last_name

    overview(){
        router.push("/")
    }
    seeGraph(){
        var pat = this.patient
        router.push({name: 'Patient-Graph', params: {pat}})
    }
}
</script>

<style scoped>

</style>