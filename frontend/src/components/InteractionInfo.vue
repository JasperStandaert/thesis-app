<template>
    <div class="interInfo">
        <p>{{drugA}} - {{drugB}}</p>
        <button @click="show = !show">Show more information</button>
        <div v-if="show">
            <p>{{desc}}</p>
        </div>
    </div>  
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'

    @Component({
        components: {

        },
        props: ['drugA', 'drugB', 'desc']
    })

export default class InteractionInfo extends Vue{
    interaction = this.$props.interaction
    show = false
}
</script>

<style scoped>

</style>