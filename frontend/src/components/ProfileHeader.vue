<template>
    <div class="navbar">
        <h1 class="name">{{first_name}} {{last_name}}</h1>
        <div class="patients">
            <v-btn elevation="2" color="cyan" class="button" @click="overview">Patients</v-btn>
        </div>
        <div class="tabs">
            <vs-tabs alignment="right">
                <vs-tab label="Patient profile">
                    <div>
                    </div>
                </vs-tab>
                <vs-tab label="Interaction graph">
                    <div>
                    </div>
                </vs-tab>
            </vs-tabs>
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

fixed-header{
    background-color: #2e6dff;
}
.tabs{
    position: relative;
    top: 0;
}

</style>