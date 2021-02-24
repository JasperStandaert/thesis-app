<template>
    <div>
        <vs-card class="patientcard">
            <div>
                <img src="../assets/face.svg" style="height: 150px; width: 125px;" alt="Profile picture" id="profile">
            </div>
            <v-card-title class="my-title">
                {{patient.first_name}} {{patient.last_name}}
            </v-card-title>
            <v-card-text class="my-content">
                <div class="patText">
                    Age: {{patient.age}}<br>
                    Gender: {{patient.gender}}
                </div>
            </v-card-text>
        </vs-card>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'

@Component({
    components: {

    },
    props: ['patient'],
})
export default class PatientCard extends Vue{
    patient = this.$props.patient

}
</script>

<style scoped>
.patientcard{
    height: 95vh;
}

img{
    width: 75px;
    height: 75px;
}

.patText{
    text-align: left;
}

.my-title{
    position: relative;
    top: 50px;
}
.my-content{
    position: relative;
    top: 50px;
}
</style>