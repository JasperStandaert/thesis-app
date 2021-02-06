<template>
    <div>
        <vs-card class="patientcard">
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

</style>