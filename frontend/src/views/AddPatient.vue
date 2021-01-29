<template>

    <div>
        <!--
        <return/>
        <form id="addPatient" @submit="checkPatient()" method="post">
            <md-field>
                <label>First Name:</label>
                <md-input v-model="first_name" required></md-input>
                <span class="md-error">First name required</span>
            </md-field>
            <md-field>
                <label>Last Name:</label>
                <md-input v-model="last_name" required></md-input>
                <span class="md-error">Last name required</span>
            </md-field>
            <md-field>
                <label>Age:</label>
                <md-input v-model="age" required></md-input>
                <span class="md-error">Age required</span>
            </md-field>
            <tags-input element-id="tags"
                v-model="selectedMeds"
                :existing-tags="this.medication"
                :typeahead="true"
                :typeahead-hide-discard="true"
                :only-existing-tags="true"
                placeholder = "Add medication for the new patient">
            </tags-input>
        </form>
-->

        <vs-card>
            <v-container fluid>
                <v-row align="center">
                    <v-col cols="12">
                        <v-autocomplete
                            v-model="selectedMeds"
                            :items="medication"
                            outlined
                            dense
                            chips
                            small-chips
                            label="outlined"
                            item-text="Medication"
                            multiple>
                        </v-autocomplete>
                    </v-col>
                </v-row>
            </v-container>
        </vs-card>
    </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.12/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@voerro/vue-tagsinput@2.4.3/dist/voerro-vue-tagsinput.js"></script>

<script lang ="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'
import Return from '../components/Return.vue'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components:{
        Return,
    }
})
export default class AddPatient extends Vue {

    first_name = ''
    last_name = ''
    age = 0

    selectedMeds: any = []
    medication: any = []
    checkPatient(){
        console.log("Added patient")
    }

    mounted(){
        service.getMedication().then( (response) => {
            if(response.status == 200){
                for(var i = 0; i < response.data.length; i++){
                    this.medication.push(response.data[i].Name.toString())
                }
                console.log(this.medication.length + " drugs found")
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