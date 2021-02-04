<template>
    <div class="interInfo">
        <p>{{drugA}} - {{drugB}}</p>
        <button @click="show = !show">Show more information</button>
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

</style>