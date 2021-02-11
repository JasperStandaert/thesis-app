<template>
    <div>
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
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import MedicationCard from '../components/MedicationCard.vue'
import PatientCard from '../components/PatientCard.vue'

@Component({
    components: {
        PatientCard,
        MedicationCard,
    },
    props: ['patient']
})
export default class Profile extends Vue{
    patient: any = this.$props.patient
    
}
</script>

<style scoped>

</style>