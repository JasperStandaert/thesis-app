<template>
    <div class="navbar">
        <h1 class="name">{{patient.first_name}} {{patient.last_name}}</h1>
        <div class="patients">
            <v-btn elevation="2" color="cyan" class="button" @click="overview">Patients</v-btn>
        </div>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'
import FixedHeader from 'vue-fixed-header'

@Component({
    components: {
        FixedHeader

    },
    props: ['patient']
})

export default class ProfileHeader extends Vue{
    patient: any = this.$props.patient
    name = this.patient.first_name + '_' + this.patient.last_name


    overview(){
        router.push("/")
    }
}
</script>

<style scoped>

.navbar{
    padding: 52px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 70px;
}

.name{
    padding: 5px;
}

.patients{
    position: absolute;
    top: 0;
    left: 0;
}

.button{
    padding: 15px 32px;
    text-align: center;
    margin: 13px 12px;
    border: none;
}


</style>