<template>
    <div class="patientHeader" >
            <vs-card v-if="show">
                <div id="patient" v-on:click="patientRoute(($event, patient))">
                    <v-card-title>
                        <h1>{{patient.first_name}} {{patient.last_name}}</h1>
                        <button @click="remove(patient)" class="remove">
                            <span class="material-icons">remove_circle</span>
                        </button>
                    </v-card-title>               
                    <v-card-text>
                        <p>Age: {{patient.age}}</p>
                        <p>Number of drugs: {{patient.medication.length}}</p>
                        <p>Gender: {{patient.gender}}</p>
                    </v-card-text>
                </div>
            </vs-card> 
    </div>
</template>

<script lang = "ts">
import {Component, Vue} from 'vue-property-decorator';
import router from '../router';
import HttpService from '../service'
import store from '../store'
const service = new HttpService()

@Component({
    components: {

    },
    props: ['patient'],
})
export default class PatientHeader extends Vue {

    public patient: any = this.$props.patient;
    public name = this.patient.first_name + "_" + this.patient.last_name
    public show = true

    public patientRoute(patient: any, e: any) {
        const pat: any = this.patient;
        router.push({name: 'Patient', params: { pat }});
        store.commit('addPatient', patient)
    }

    remove(){
        
        service.removePatient(this.name).then((response)=>{
            if(response.status == 200){
                console.log(response.data)
                this.show = false   
                Vue.nextTick()
            }
        }).catch((error) =>{
            console.log(error)
        });
    }

}
</script>

<style scoped>

h1{
    font-size: 24px;
}

#patient{
    text-align: left;
    align-content: center;
}

.remove{
    position: relative;
    color: red;
    top: 5px;
    left: 15px;
}
.material-icons{
    font-size: 30px;
}
.material-icons:hover{
    background-color: black;
    border-radius: 28px;
    border-width: 2px;;
}

.patientHeader:hover{
    box-shadow: 5px 10px 50px 10px #888888;
}

</style>