<template>
    <div class="interInfo">
        <p>{{drugA}} - {{drugB}}</p>
        <div @click="show = !show" class="interactionButton">
            <img v-if="!show" src="../assets/expand.svg" alt="expand">
            <img v-else src="../assets/collapse.svg" alt="Collapse">
        </div>
        <div v-if="show">
            <p>{{description}}</p>
        </div>
        <v-divider/>
    </div>  
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import HttpService from '../service'

const service = new HttpService();

    @Component({
        components: {

        },
        props: ['drugA', 'drugB']
    })

export default class InteractionInfo extends Vue{
    drugA = this.$props.drugA
    drugB = this.$props.drugB
    description: string = ""
    show = false

    mounted(){
        service.getInteractionDescription(this.drugA, this.drugB).then((response) =>{
            if(response.status == 200){
                this.description = response.data.toString()
            }
        }).catch((error)=> {

        });
    }
}
</script>

<style scoped>
.interactionButton{
    justify-content: flex-end;
    display: flex;
}
</style>