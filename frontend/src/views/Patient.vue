<template>
    <div id="patient">
        <div id="header">
                <h1 class="name">{{patient.first_name}} {{patient.last_name}}</h1>
                 <div class="patients">
                    <v-btn elevation="2" color="cyan" class="button" @click="overview">Patients</v-btn>
                </div>
            </div>
        <div id="section1">
            <div id="arrow">
                <a href="#section2" id="downArrow"><span class="material-icons">arrow_downward</span></a>
            </div>
            <div id="profile">
                <profile :patient="patient"/>
            </div>
        </div>
        <div id="section2">
            <a href="#header"><span class="material-icons">arrow_upward</span></a>
            <div id="interactions">
                <interactions :patient="patient"/>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Profile from '../components/Profile.vue'
import Interactions from '../components/Interactions.vue'
import router from "../router"
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';
import store from '../store'

const service = new HttpService();

@Component({
    components: {
        Profile,
        Interactions,
    },
    props: ['patient'],
})


export default class Patient extends Vue {
    patient = store.getters.patient

    interactions = false
    profile = true

    overview(){
        router.push("/")
    }
}
</script>

<style scoped>
#arrow{
    position: relative;

}
.material-icons{
    position: relative;
    left: 650px;
    top: 10px;
}
#header{
    position: relative;
    width: 100%;
    padding: 52px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 70px;
    z-index: 999;
}
.patients{
    position: absolute;
    top: 0;
    left: 0;
}
.button{
    position: absolute;
    top: 0;
    left: 0;
    margin: 40px 15px;;
}
html{
    scroll-behavior: smooth;
}
#section1{
    position: relative;
}

#section2{
    position: relative;
    margin-top: 320px;
}
#profile{
    height: 750px;
    margin-top: 10px;
}
#interactions{
    height: 750px;
}

</style>