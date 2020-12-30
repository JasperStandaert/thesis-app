<template>
    <div id="graph">
        <cytoscape :config="config">
            <cy-element
    v-for="def in elements"
    :key="`${def.data.id}`"
    :definition="def"
    v-on:mousedown="deleteNode($event, def.data.id)"
  />
        </cytoscape>
    </div> 
</template>

<script src="cytoscape.min.js"></script>
<script>
import { Component, Vue } from 'vue-property-decorator'

export default class PatientGraph extends Vue{
    config = {
        style: [
            {
            selector: 'node',
            style: {
                'background-color': '#666',
                'label': 'data(id)'
            }
            }, {
            selector: 'edge',
            style: {
                'width': 3,
                'line-color': '#ccc',
                'target-arrow-color': '#ccc',
                'target-arrow-shape': 'triangle'
            }
        }
        ],
        layout: {
            name: 'grid',
            rows: 1
        }
    }
    elements = [
        {
            data: {id: 'a'}
        },
        {
            data: {id: 'b'}
        }
    ]
};
</script>
<style scoped>

</style>