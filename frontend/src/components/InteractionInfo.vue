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
            <div v-if="show">
                <p>{{description}}</p>
            </div>
        </vs-card>
    </div>  
</template>

<script lang="ts">
import {Component, Vue, Watch} from 'vue-property-decorator'
import HttpService from '../service'
import store from '../store'

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
        Vue.nextTick();
    }

    @Watch(store.state.activeNode)
    onNodeClick(){
         if(this.drugA === store.state.activeNode || this.drugB === store.state.activeNode){
            this.show = true
        }
        console.log("Node gevonden")
    }

    @Watch(store.getters.activeInteraction)
    onInteractionClick(){
         if(this.drugA === store.state.activeInteraction[0] || this.drugA === store.state.activeInteraction[1]){
            this.show = true
        } else if (this.drugB === store.state.activeInteraction[0] ||this.drugB === store.state.activeInteraction[1]){
            this.show = true
        } else{
            this.show = false
        }

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