<template>
    <div>
        <div>
            <img src="../assets/face.svg" style="height: 150px; width: 125px;" alt="Profile picture" id="profile">
        </div>
            <h1>
                {{patient.first_name}} {{patient.last_name}}
            </h1>
        <div class="my-content">
            <div class="patText">
                <p><h3>Age:</h3> {{patient.age}}</p>
                <p><h3>Gender: </h3>{{patient.gender}}</p>
            </div>
        </div>
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
    align-content: center;
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