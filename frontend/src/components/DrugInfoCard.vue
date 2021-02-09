<template>
    <div class='drugBar' v-if="!isRemoved" >
        <div>
            <h3 class="med">
                {{drug.Name}}
                <img v-if="!show" src="../assets/expand.svg" alt="expand" @click="show = !show">
                <img v-else src="../assets/collapse.svg" alt="Collapse" @click="show = !show">
            </h3>
            <img src="../assets/remove.svg" class="remove"/>
        </div>
        <div v-if="show">
            <h3>Description: </h3>
            <p>{{drug.Description}}</p>
            <h3>Indication: </h3>
            <p>{{drug.Indication}}</p>
            <h3>Toxicity: </h3>
            <p>{{drug.Toxicity}}</p>
        </div>
        <v-divider/>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {

    },
    props: ['drug', 'patient'],
})

export default class DrugInfoCard extends Vue{
    drug = this.$props.drug
    pat = this.$props.patient
    public show = false
    public isRemoved = false

    remove(med: string, name: string){
        service.removeDrug(name, med).then( (response) =>{
            if(response.status == 200){
                console.log("succesfully removed");
                this.isRemoved = true
                Vue.nextTick()
            }
        }).catch((error)=>{
            console.log(error)
        })
    }
}
</script>

<style scoped>

#drugBar{
    border-width: 2px;
    border-style: solid;
    border-color: darkgrey;
    text-align: left;
}
.med{
    text-align: left;
}
.remove{
    position: relative;
    left: 245px;
}

</style>