<template>
    <div class="profileheader">
        <h1 class="name">{{first_name}} {{last_name}}</h1>
        <p align="left">
            <button class="patients" @click="overview">Patients</button>
        </p>
    </div>
    
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'

@Component({
    components: {

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

.profileheader{
    padding: 30px;
    text-align: center;
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

</style>