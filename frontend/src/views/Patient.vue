<template>
    <div id="patient">
        <v-container>
            <v-row>
                <v-col cols="6">
                    <medication-card/>
                </v-col>
                <v-col cols="6">
                    <interaction-card/>
                </v-col>
            </v-row>
        </v-container>
        <p @click="check()">Hello {{patient.first_name}}</p>
        <patient-graph/>
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
    public patient: any =  this.$route.params.pat;

    public check() {
        console.log(this.patient == null);
    }
}
</script>

<style scoped>

</style>