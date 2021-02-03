<template>
    <div class="patientform">
        <return/>
        <form id="addPatient">
            <md-field>
                <label>First Name:</label>
                <md-input v-model="patient.first_name" required></md-input>
                <span class="md-error">First name required</span>
            </md-field>
            <md-field>
                <label>Last Name:</label>
                <md-input v-model="patient.last_name" required></md-input>
                <span class="md-error">Last name required</span>
            </md-field>
            <md-field>
                <label>Age:</label>
                <md-input v-model="patient.age" required></md-input>
                <span class="md-error">Age required</span>
            </md-field>
            <md-field>
                <label for="medication"></label>
                <multi-select
                id="medication"
                class="medication"
                v-model="patient.medication"
                :options="meds"
                :multiple="true"
                :close-on-select="true"
                :clear-on-select="false"
                placeholder="Search for medication">
                </multi-select>
            </md-field>
            <md-button class="md-raised md-primary" style="align-items: center; margin: 20px 0 0 0;" :value="this.buttonVal" v-on:click=patientClick()>
                Add Patient
            </md-button>
        </form>
    </div>
</template>

<script src="https://unpkg.com/vue-multiselect@2.1.0"></script>
<script lang ="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'
import Return from '../components/Return.vue'
import MultiSelect from 'vue-multiselect'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components:{
        Return,
        MultiSelect,
    }
})
export default class AddPatient extends Vue {

    buttonVal = 'Add patient'

    fn = ''
    ln = ''
    a = 0
    patient =  {
        first_name: '',
        last_name: '',
        age: 0,
        medication: []
        }
    meds: any = []
    patientClick(){
        service.postPatient(this.patient).then( (response) =>{
            if(response.status == 200){
                console.log("Added patient succesfully")
                router.push("/")
            }
        }).catch((error) => {
            console.log(error);
        });
    }

    mounted(){
        service.getMedication().then( (response) => {
            if(response.status == 200){
                for(var i = 0; i < response.data.length; i++){
                    this.meds.push(response.data[i].Name.toString())
                }
                console.log(this.meds.length + " drugs found")
            }
        }).catch((error) => {
            console.log("ERROR:");
            console.log(error);
        });
    }
}
</script>
<style scoped>

</style>