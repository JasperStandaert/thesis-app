<template>
    <div class="patientHeader" >
        <vs-card >
            <vs-card v-on:click="patientRoute(($event, patient))">
                <v-card-title>
                    {{patient.first_name}} {{patient.last_name}}
                </v-card-title>
                <v-card-text>
                    <p>Age: {{patient.age}}</p>
                    <p>Number of drugs: {{patient.medication.length}}</p>
                </v-card-text>
            </vs-card>
            <vs-card>
                <button @click="remove(patient)">Remove this patient</button>
            </vs-card>
        </vs-card>  
    </div>
</template>

<script lang = "ts">
import {Component, Vue} from 'vue-property-decorator';
import router from '../router';
import HttpService from '../service'

const service = new HttpService()

@Component({
    components: {

    },
    props: ['patient'],
})
export default class PatientHeader extends Vue {

    public patient: any = this.$props.patient;
    public name = this.patient.first_name + "_" + this.patient.last_name

    public patientRoute(patient: any, e: any) {
        const pat: any = this.patient;
        router.push({name: 'Patient', params: { pat }});
    }

    remove(){
        
        service.removePatient(this.name).then((response)=>{
            if(response.status == 200){
                console.log(response.data)
            }
        }).catch((error) =>{
            console.log(error)
        });
    }
}
</script>

<style scoped>

</style>