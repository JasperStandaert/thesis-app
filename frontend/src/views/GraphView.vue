<template>
    <div>
        <profile-header :fn='patient.first_name' :ln='patient.last_name'/>
        <button @click='goBack()'>Back to patient</button>

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
import ProfileHeader from '../components/ProfileHeader.vue'
import router from '../router'

@Component({
    components: {
        PatientGraph,
        InteractionCard,
        ProfileHeader,
    },
    props: ['patient'],
})
export default class GraphView extends Vue {
    patient:any = this.$route.params.pat

    name = this.patient.first_name + "_" + this.patient.last_name

    goBack(){
        var pat = this.patient
        router.push({name: 'Patient', params: {pat}})
    }
    
}
</script>

<style scoped>

</style>