<template>
    <div id="sidebar">
        <button v-on:click="Search">Search</button>
    </div>
    
</template>
<script>
export default {

    search() {
        router.push('/search');
    },
};
</script>
<style scoped>

</style>