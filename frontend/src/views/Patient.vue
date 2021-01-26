<template>
    <div id="patient">
        <return/>
        <medication-card/>
        <interaction-card/>
    </div>
</template>
<script lang="ts">
import MedicationCard from "../components/MedicationCard.vue"
import InteractionCard from "../components/InteractionCard.vue"
import Return from "../components/Return.vue"
import { Component, Vue } from 'vue-property-decorator';

@Component({
    components: {
        MedicationCard,
        InteractionCard,
        Return,
    }
})
export default class Patient extends Vue{
};
</script>

<style scoped>

</style>