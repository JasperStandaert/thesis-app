<template>
    <vs-card>
        <v-card-title>
            Medication for {{patient}}
        </v-card-title>
        <v-card-text>
            <div v-for="(med, i) in medication" :key="i">
                <p>{{med.Name}}</p>
                <button @click="remove(med.Name)">Remove this drug</button>
            </div>
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
    props: ['medication', 'pat_name']
})
export default class MedicationCard extends Vue {
    medication: any = this.$props.medication
    patient: any = this.$props.pat_name

    remove(med: any){
        service.removeDrug(this.patient, med).then( (response) =>{
            if(response.status == 200){
                console.log("succesfully removed")
            }
        }).catch((error)=>{
            console.log(error)
        })
    }
}
</script>

<style scoped>

</style>