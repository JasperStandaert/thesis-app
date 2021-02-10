<template>
    <div class="interInfo">
        <vs-card>
            <v-card-title>
                <p>
                    {{drugA}} - {{drugB}}
                    <img v-if="!show"  @click="show = !show" src="../assets/expand.svg" alt="expand">
                    <img v-else  @click="show = !show" src="../assets/collapse.svg" alt="Collapse">
                </p>
            </v-card-title>
        </vs-card>
        <div v-if="show">
            <p>{{description}}</p>
        </div>
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
.inter{
    text-align: left;
}

p{
    text-align: left;
    font-size: 15px;
}
</style>