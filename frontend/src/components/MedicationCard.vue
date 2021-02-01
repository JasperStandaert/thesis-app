<template>
    <vs-card>
        <v-card-title>
            Medication
        </v-card-title>
        <v-card-text>
            <ul>
                <li v-for="(med, i) in medication" :key="i+1" :drug='med'>
                    <p @click="showInfo(med)">{{med.Name}}</p>
                </li>
            </ul>
        </v-card-text>
    </vs-card>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import router from '../router'
@Component({
    components: {
    },
    props: ['medication']
})
export default class MedicationCard extends Vue {
    medication: any = this.$props.medication

    showInfo(drug: any){
        console.log("boop")
    }
}
</script>

<style scoped>

</style>