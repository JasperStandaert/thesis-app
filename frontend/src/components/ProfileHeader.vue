<template>
    <div class="navbar">
        <h1 class="name">{{first_name}} {{last_name}}</h1>
        <p align="left">
            <v-btn elevation="2" color="cyan" class="patients" @click="overview">Patients</v-btn>
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
    padding: 20px;
    color: white;
    font-size: 16px;
    background-color: #2e6dff;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 70px;
}

.name{
    padding: 5px;
}

fixed-header{
    background-color: #2e6dff;
}

</style>