<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="7">
                    <patient-graph :patient="name"/>
                </v-col>
                <v-col cols="5">
                    <interaction-card :patient="name"/>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import PatientGraph from '../components/PatientGraph.vue'
import InteractionCard from '../components/InteractionCard.vue'

@Component({
    components: {
        PatientGraph,
        InteractionCard,
    },
    props: ['patient']

})
export default class Interactions extends Vue{
    patient = this.$props.patient
    name = this.patient.first_name + "_" + this.patient.last_name
    
}
</script>