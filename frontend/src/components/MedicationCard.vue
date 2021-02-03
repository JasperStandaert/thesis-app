<template>
    <vs-card height="00px" max-height="300px">
        <v-card-title>
            Medication
        </v-card-title>
        <drug-info-card v-for="(med, i) in medication" :key="i" :drug="med" :patient="pat_name"/>
        <v-card-text>
            <button @click="addDrug(patient)">Add drug</button>
        </v-card-text>
    </vs-card>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import DrugInfoCard from '../components/DrugInfoCard.vue'
import router from '../router'
import HttpService from '../service'

const service = new HttpService();
@Component({
    components: {
        DrugInfoCard
    },
    props: ['medication', 'patient']
})
export default class MedicationCard extends Vue {
    medication: any = this.$props.medication
    patient: any = this.$props.patient
    public show = true

    pat_name = this.patient.first_name + "_" + this.patient.last_name

    addDrug(patient: any){
        router.push({name: "AddDrug", params: {patient}})
    }
}
</script>

<style scoped>

</style>