<template>
    <div class="patientHeader" v-on:click="patientRoute(($event, patient))">
        <vs-card>
            <v-card-title>
                {{patient.first_name}} {{patient.last_name}}
            </v-card-title>
            <v-card-text>
                <p>Age: {{patient.age}}</p>
                <p>Condition: {{patient.condition}}</p>
            </v-card-text>
        </vs-card>
    </div>
</template>

<script lang = "ts">
import {Component, Vue} from 'vue-property-decorator';
import router from '../router';

@Component({
    components: {

    },
    props: ['patient'],
})
export default class PatientHeader extends Vue {

    public patient: any = this.$props.patient;

    public patientRoute(patient: any, e: any) {
        const pat: any = this.patient;
        router.push({name: 'Patient', params: { pat }});
    }
}
</script>

<style scoped>

</style>