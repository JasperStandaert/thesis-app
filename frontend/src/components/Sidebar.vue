<template>
    <div id="sidebar">
        <button v-on:click="Search">Search</button>
    </div>
    
</template>
<script>
import router from "../router"
import { Component, Vue } from 'vue-property-decorator'
export default class Search extends Vue{

    search() {
        router.push('/search');
    }
};
</script>
<style scoped>

</style>