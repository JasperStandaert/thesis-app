<template>
    <div id="patient">
        <v-container>
            <v-row>
                <v-col cols="6">
                    <medication-card :medication="patient.medication"/>
                </v-col>
                <v-col cols="6">
                    <interaction-card :patient="name"/>
                </v-col>
            </v-row>
        </v-container>
        <p>Hello {{patient.first_name}}</p>
        <!--<patient-graph :patient="patient"/>-->
        <return/>
    </div>
</template>
<script lang="ts">
import MedicationCard from '../components/MedicationCard.vue';
import InteractionCard from '../components/InteractionCard.vue';
import PatientGraph from '../components/PatientGraph.vue';
import Return from '../components/Return.vue';
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {
        MedicationCard,
        InteractionCard,
        PatientGraph,
        Return,
    },
    props: ['patient'],
})


export default class Patient extends Vue {
    patient: any =  this.$route.params.pat;
    name = this.patient.first_name + "_" + this.patient.last_name
}
</script>

<style scoped>

</style>