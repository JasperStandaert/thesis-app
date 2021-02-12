
<template>
    <div id="addDrug">
        <div class="header">
            <h1>Add a drug for {{patient.first_name}}</h1>
             <v-btn class="button" @click="patBack(name)">Back to patient</v-btn>
        </div>
        <div class="content">
            <vs-card>
                <v-card-content>
                    <form>
                        <md-field>
                            <p for="medication">Medication:</p><br>
                            <multi-select
                                id="medication"
                                class="medication"
                                v-model="medication"
                                :options="items"
                                placeholder="Add a medication">
                            </multi-select>
                        </md-field>
                        <md-button class="md-raised md-primary" style="align-items: center; margin: 20px 0 0 0;" :value="this.buttonVal" v-on:click="addDrug(name, patient, medication)">
                            Add Drug
                        </md-button>
                    </form>
                </v-card-content>
            </vs-card>
        </div>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import MultiSelect from 'vue-multiselect'
import router from '../router'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components: {
        MultiSelect
    },
    props: ['patient']
})
export default class AddDrug extends Vue{
    patient: any = this.$route.params.patient
    name = this.patient.first_name + "_" + this.patient.last_name
    medication: any = []
    items: any = []
    
    mounted(){
        console.log(this.patient.first_name)
        service.getMedication().then((response) => {
            if(response.status == 200){
                for (var i = 0; i < response.data.length; i++){
                    this.items.push(response.data[i].Name)
                }
            }
        }).catch((error) =>{
            console.log(error)
        });
    }

    addDrug(name: string, patient: any, med: any){
        patient = this.patient
        service.addDrug(name, med).then((response) =>{
            if(response.status == 200){
                this.patBack(name);
            }
        }).catch((error) =>{
            console.log(error)
        })
    }

    patBack(name: string){
        service.getPatient(name).then((response) => {
            if(response.status == 200){
                var pat = response.data
                router.push({name: 'Patient', params: {pat}})
            }
        }).catch((error) =>{
            console.log(error)
        });
    }
}
</script>

<style scoped>

.header{
    padding: 52px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 70px;
}

.button{
    position: absolute;
    top: 0;
    left: 0;
    margin: 40px 15px;;
}

.content{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 12px;
}

</style>