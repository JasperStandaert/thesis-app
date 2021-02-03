<template>
    <vs-card height="00px" max-height="300px">
        <v-card-title>
            Medication
        </v-card-title>
        <v-card-text>
            <div v-for="(med, i) in medication" :key="i">
                <p v-if="show">{{med.Name}}</p>
                <button @click="remove(med.Name)">Remove this drug</button>
            </div>
        </v-card-text>
        <v-card-text>
            <button @click="addDrug(patient)">Add drug</button>
        </v-card-text>
    </vs-card>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'
import HttpService from '../service'

const service = new HttpService();
@Component({
    components: {
    },
    props: ['medication', 'patient']
})
export default class MedicationCard extends Vue {
    medication: any = this.$props.medication
    patient: any = this.$props.patient
    public show = true

    pat_name = this.patient.first_name + "_" + this.patient.last_name

    remove(med: any){
        service.removeDrug(this.pat_name, med).then( (response) =>{
            if(response.status == 200){
                console.log("succesfully removed");
                this.show = false
                Vue.nextTick();
            }
        }).catch((error)=>{
            console.log(error)
        })
    }

    addDrug(patient: any){
        router.push({name: "AddDrug", params: {patient}})
    }
}
</script>

<style scoped>

</style>