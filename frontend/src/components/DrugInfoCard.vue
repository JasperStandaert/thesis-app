<template>
    <div class='drugBar' v-if="!isRemoved" >
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <vs-card>
            <v-title>
                <h3>
                    {{drug.Name}}
                    <img v-if="!show" src="../assets/expand.svg" alt="expand" @click="show = !show">
                    <img v-else src="../assets/collapse.svg" alt="Collapse" @click="show = !show">
                </h3>
            </v-title>
            <v-text>
                <div v-if="show">
                    <h3>Description: </h3>
                    <p>{{drug.Description}}</p>
                    <h3>Indication: </h3>
                    <p>{{drug.Indication}}</p>
                    <h3>Toxicity: </h3>
                    <p>{{drug.Toxicity}}</p>
                </div>
            </v-text>
            <v-card-actions>
                <button @click="remove(drug.Name, pat)" class="remove">
                    <span class="material-icons">remove_circle</span>
                </button>
            </v-card-actions>
        </vs-card>
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
    left: 480px;
    color: red;
    top: -10px;
}
.material-icons{
    font-size: 30px;
}
.material-icons:hover{
    background-color: black;
    border-radius: 30px;
    border-width: 2px;;
}
</style>