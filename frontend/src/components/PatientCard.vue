<template>
    <div>
        <vs-card class="patientcard">
            <div>
                <img src="../assets/face.svg" alt="Profile picture" id="profile">
            </div>
            <v-card-title>
                {{patient.first_name}} {{patient.last_name}}
            </v-card-title>
            <v-card-text>
                Age: {{patient.age}}
            </v-card-text>
        </vs-card>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'

@Component({
    components: {

    },
    props: ['patient'],
})
export default class PatientCard extends Vue{
    patient = this.$props.patient

}
</script>

<style scoped>
.patientcard{
    height: 200px;
}

img{
    width: 75px;
    height: 75px;
}
</style>