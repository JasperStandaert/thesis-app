<template>
    <div class="cardContainer">
        <vs-card>
            <v-card-title>
                <h2>New patient</h2>
            </v-card-title>
            <v-card-text>
                <div>
                    <form class="form">
                         <div class="md-layout md-gutter">
                            <div class="md-layout-item md-medium-size-150">
                                <md-field>
                                    <label for="first-name">First Name:</label>
                                    <md-input name="first-name" id="first-name" autocomplete="given-name" v-model="patient.first_name"></md-input>
                                    <span class="md-error">First name required</span>
                                </md-field>
                            </div>
                            <div class="md-layout item md-medium-size-150">
                                <md-field>
                                    <label for="last-name">Last Name:</label>
                                    <md-input name="last-name" id="last-name" v-model="patient.last_name"></md-input>
                                    <span class="md-error">Last name required</span>
                                </md-field>
                            </div>
                        </div>
                        <div class="md-layout md-gutter">
                            <div class="md-layout-item md-small-size-100">
                                <md-field>
                                    <label for="age">Age:</label>
                                    <md-input name="age" id="age" v-model="patient.age"></md-input>
                                    <span class="md-error">Age required</span>
                                </md-field>
                            </div>
                            <div class="md-layout-item md-small-size-100">
                                    <label for="gender">Gender:</label>
                                    <multi-select name="gender" id="gender" v-model="patient.gender" :options='options'></multi-select>
                            </div>
                        </div>
                        <div class="md-layout md-gutter">
                                <label for="medication">Medication:</label>
                                <multi-select
                                    id="medication"
                                    name
                                    v-model="patient.medication"
                                    :options="meds"
                                    :multiple="true"
                                    placeholder="Search for medication">
                                </multi-select>
                        </div>
                     </form>
                </div>
            </v-card-text>
            <v-card-actions>
                <v-btn @click='patientClick()'>Add patient</v-btn>
            </v-card-actions>
        </vs-card>
    </div>
    
</template>
<script src="https://unpkg.com/vue-multiselect@2.1.0"></script>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import MultiSelect from 'vue-multiselect'
import HttpService from '../service'
import router from '../router'

const service = new HttpService();

@Component({
    components: {
        MultiSelect,
    },
})

export default class AddPatientCard extends Vue {
    buttonVal = 'Add patient'
    options = ['Male', 'Female', 'Other']

    fn = ''
    ln = ''
    a = 0
    g = ''
    patient =  {
        first_name: '',
        last_name: '',
        age: 0,
        medication: [],
        gender: ''
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
                    this.meds.push(response.data[i].Name)
                }
                console.log("drug: ", this.meds[5])
                console.log(this.meds.length + " drugs found")
            }
        }).catch((error) => {
            console.log("ERROR:");
            console.log(error);
        });
    }

    
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>

v-card-actions{
    align-content: center;
    display: flex;
    justify-content: center;
}

</style>