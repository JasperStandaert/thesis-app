<template>
    <vs-card height="300px" max-height="300px">
        <v-card-title>
            Interactions
        </v-card-title>
        <v-card-text>
            <p v-for="(inter, i) in interactions" :key="i+1">{{inter[0]}} - {{inter[1]}}</p>
        </v-card-text>
    </vs-card>
</template>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import HttpService from '../service'

const service = new HttpService();

@Component({
    components: {

    },
    props: ['patient']
})
export default class InteractionCard extends Vue {
    patientName = this.$props.patient
    interactions: any = []

    mounted(){

        service.getInteractions(this.patientName).then((response) =>{
            if(response.status == 200){
                this.interactions = response.data
            }
        }).catch((error) =>{
            console.log(error)
        })
    }
}
</script>
<style scoped>

</style>