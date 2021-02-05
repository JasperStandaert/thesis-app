<template>
    <div class="navbar">
        <h1 class="name">{{first_name}} {{last_name}}</h1>
        <p align="left">
            <button class="patients" @click="overview">Patients</button>
        </p>
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
    props: ['fn', 'ln']
})

export default class ProfileHeader extends Vue{
    first_name = this.$props.fn
    last_name = this.$props.ln

    overview(){
        router.push("/")
    }
}
</script>

<style scoped>

.navbar{
    padding: 30px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
}

.name{
    padding: 5px;
}

.patients{
    padding: 0px 0px 2px 2px;
    margin-bottom: 10px
}

.navbar.vue-fixed-header--isFixed{
    text-align: center;
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    
}

fixed-header{
    background-color: #2e6dff;
}

</style>