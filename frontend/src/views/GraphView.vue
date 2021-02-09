<template>
    <div>
        {{patient.first_name}}
        <button @click='goBack()'>Back to patient</button>
    </div> 
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'

@Component({
    components: {

    },
    props: ['patient'],
})
export default class GraphView extends Vue {
    patient = this.$route.params.patient

    goBack(){
        var pat = this.patient
        router.push({name: 'Patient', params: {pat}})
    }
    
}
</script>

<style scoped>

</style>