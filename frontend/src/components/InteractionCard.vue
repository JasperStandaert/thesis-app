<template>
    <vs-card outlined class="interactionCard">
        <v-card-title class="title">
            Interactions
        </v-card-title>
        <v-divider/>
        <interaction-info v-for="(inter, i) in interactions" :key="i+1" :drugA="inter[0]" :drugB="inter[1]" :desc="inter[2]"/>
    </vs-card>
</template>
<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import HttpService from '../service'
import InteractionInfo from '../components/InteractionInfo.vue'

const service = new HttpService();

@Component({
    components: {
        InteractionInfo,
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

.interactionCard{
    height: 250px;
    width: 300px;
    overflow-y: scroll;
}

</style>