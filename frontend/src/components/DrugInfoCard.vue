<template>
    <div class='drugBar' v-if="!isRemoved">
        <h2>{{drug.Name}}</h2>
        <button @click="show = !show">Show more information</button>
        <button @click="remove(drug.Name, pat)">Remove</button>
        <div v-if="show">
            <h3>Description: </h3>
            <p>{{drug.Description}}</p>
            <h3>Indication: </h3>
            <p>{{drug.Indication}}</p>
            <h3>Toxicity: </h3>
            <p>{{drug.Toxicity}}</p>
        </div>
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
}

</style>