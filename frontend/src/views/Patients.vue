<template>
    <div id="patientOverview">
        <program-header/>
        <div class="content">
             <v-btn elevation="2" class="addBtn" @click="addPatient()">Add a new patient</v-btn>
            <PatientHeader class='patient' v-for="(patient, i) in patients" :key="i+1" :patient='patient'/>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import PatientHeader from '../components/PatientHeader.vue';
import ProgramHeader from '../components/ProgramHeader.vue'
import store from '../store';
import router from '../router';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {
        PatientHeader,
        ProgramHeader,
    },
})
export default class Patients extends Vue {

    public patients = [];
    public loading = true;
    public error = false;

    public addPatient() {
        router.push('/add_patient');
    }

    public mounted() {
        service.getPatients().then( (response) => {
            if (response.status == 200) {
                console.log('Patients found');
                store.commit('addPatients', response.data);
                this.patients = response.data;
            }
        }).catch((error) => {
            this.loading = false;
            this.error = true;
            console.log('ERROR:');
            console.log(error);
        });
    }
}
</script>

<style scoped>

.addBtn{
    margin: 10px 10px;
}

</style>