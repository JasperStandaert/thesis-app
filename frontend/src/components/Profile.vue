<template>
    <div>
        <vs-card>
            <v-card-content>
                <patient-card :patient="patient"/>
                <medication-card :medication="patient.medication" :patient="patient"/>
            </v-card-content>
        </vs-card>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import MedicationCard from '../components/MedicationCard.vue'
import PatientCard from '../components/PatientCard.vue'
import store from '../store'

@Component({
    components: {
        PatientCard,
        MedicationCard,
    },
    props: ['patient']
})
export default class Profile extends Vue{
    patient = store.getters.patient
    
}
</script>

<style scoped>

medication-card{
    margin-top: 200px;
}

</style>