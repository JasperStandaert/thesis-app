<template>
    <div id="patientOverview">
        <p>Patients overview</p>
        <sidebar/>
        <dl>
            <dt v-on:click="patient()">Patient 1</dt>
            <dd>Naam Leeftijd</dd>
            <dt v-on:click="patient()">Patient 2</dt>
            <dd>Naam Leeftijd</dd>
            <dt v-on:click="patient()">Patient 3</dt>
            <dd>Naam Leeftijd</dd>
        </dl>
    </div>
</template>

<script lang="ts">
import Sidebar from "../components/Sidebar.vue";
import { Component, Vue } from 'vue-property-decorator';
import router from "../router";

@Component({
    components: {
        Sidebar,
    }
})
export default class Patients extends Vue {
    
    patient(){
        router.push("/patient");
    }
}
</script>

<style scoped>

</style>