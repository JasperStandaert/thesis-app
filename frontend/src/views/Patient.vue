<template>
    <div id="patient">
        <p>Patient profile page</p>
        <div>
            <patient-graph/>
        </div>
    </div>
</template>
<script lang="ts">
import PatientGraph from "../components/PatientGraph.vue";
import { Component, Vue } from 'vue-property-decorator';

@Component({
    components: {
        PatientGraph,
    }
})
export default class Patient extends Vue{
};
</script>

<style scoped>

</style>