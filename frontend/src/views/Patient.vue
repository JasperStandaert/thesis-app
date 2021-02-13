<template>
    <div id="patient">
        <div id="header">
            <h1 class="name">{{patient.first_name}} {{patient.last_name}}</h1>
            <div class="patients">
                <v-btn elevation="2" color="cyan" class="button" @click="overview">Patients</v-btn>
            </div>
            <div class="tabs">
                <v-btn @click="toggle()">{{text}}</v-btn>
            </div>
        </div>
        <transition name="fade">
            <div id="profile" v-if="profile">
                <profile :patient="patient"/>
            </div>
        </transition>
        <transition name="bounce">
            <div id="interactions" v-if="!profile">
                <interactions :patient="patient"/>
            </div>
        </transition>
    </div>
</template>
<script lang="ts">
import Profile from '../components/Profile.vue'
import Interactions from '../components/Interactions.vue'
import router from "../router"
import { Component, Vue } from 'vue-property-decorator';
import HttpService from '../service';

const service = new HttpService();

@Component({
    components: {
        Profile,
        Interactions,
    },
    props: ['patient'],
})


export default class Patient extends Vue {
    patient: any =  this.$route.params.pat;
    text = "Interactions"

    interactions = false
    profile = true

    overview(){
        router.push("/")
    }
    seeGraph(){
        var pat = this.patient
        router.push({name: 'Patient-Graph', params: {pat}})
    }
    toggle(){
        this.profile = !this.profile
        if(this.profile){
            this.text="Interactions"
        } else{
            this.text = "Profile"
        }
    }
}
</script>

<style scoped>

#header{
    padding: 52px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 70px;
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

.bounce-enter-active {
    animation: bounce-in .5s;
}

.bounce-leave-active{
    animation: bounce-in .5s reverse;
}

@keyframes bounce-in{
    0%{
        transform: scale(0);
    }

    50%{
        transform: scale(1.2);
    }

    100% {
        transform: scale(1);
    }
}

.tabs{
    position: absolute;
    top: 0;
    right: 0;
    margin: 40px 15px;
}

</style>