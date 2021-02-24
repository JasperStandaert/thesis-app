<template>
    
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
    height: 100vh;
}

</style>