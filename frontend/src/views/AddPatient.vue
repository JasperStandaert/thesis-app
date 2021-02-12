<template>
    <div class="addPatient">
        <div class="header">
            <h1>Add a new patient</h1>
        </div>
         <v-btn elevation="2" color="cyan" class="button" @click="overview">Patients</v-btn>
        <div class="patientform">
            <add-patient-card/>
        </div>
    </div>
</template>


<script lang ="ts">
import {Component, Vue} from 'vue-property-decorator'
import AddPatientCard from '../components/AddPatientCard.vue'
import router from '../router'

@Component({
    components:{
        AddPatientCard,
    }
})
export default class AddPatient extends Vue {

        overview(){
        router.push("/")
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

.patientform{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 12px;
}

.button{
    position: absolute;
    top: 0;
    left: 0;
    margin: 40px 15px;;
}
</style>