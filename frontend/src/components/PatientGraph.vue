<script src="https://d3js.org/d3.v4.js"></script>
<template>
    <div id="patientGraph">
        Boeh
    </div> 
</template>


<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import d3 from 'd3';
@Component({
    components: {

    },
})

export default class PatientGraph extends Vue {
    public nodes = [{id: 1, name: 'A'},
            {id: 2, name: 'B'},
            {id: 3, name: 'C'}];
    public links = [{source: 1, target: 2},
             {source: 1, target: 3}];
    public margin = {top: 10, right: 30, bottom: 30, left: 40};
    public width = 400 - this.margin.left - this.margin.right;
    public height = 400 - this.margin.top - this.margin.bottom;
    public svg = d3.select('patientGraph')
.append('svg')
  .attr('width', this.width + this.margin.left + this.margin.right)
  .attr('height', this.height + this.margin.top + this.margin.bottom)
.append('g')
  .attr('transform',
        'translate(' + this.margin.left + ',' + this.margin.top + ')');

    public link = this.svg.selectAll('line').data(this.links).enter().append('line').style('stroke', '#aaa');
    public node = this.svg.selectAll('circle').data(this.nodes).enter().append('circle').attr('r', 20).style('fill', '#69b3a2');

    public simulation = d3.forceSimulation(this.nodes).force('link', d3.forceLink().id(function(d) { return d.id; }).links(this.links));
    public ticked() {
    this.link
        .attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

    this.node
         .attr('cx', function(d) { return d.x + 6; })
         .attr('cy', function(d) { return d.y - 6; });
  }



}
</script>
<style scoped>

</style>