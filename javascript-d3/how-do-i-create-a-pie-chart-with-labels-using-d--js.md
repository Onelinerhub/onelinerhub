# How do I create a pie chart with labels using d3.js?
// plain

Creating a pie chart with labels using d3.js is very straightforward. The following example shows how to create a basic pie chart with labels.

```
// Create an array of objects with data
var data = [
    {name: 'Group A', value: 20},
    {name: 'Group B', value: 17},
    {name: 'Group C', value: 15},
    {name: 'Group D', value: 38}
];

// Set the dimensions and margins of the chart
var width = 450;
var height = 450;
var margin = 40;

// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin

// append the svg object to the div called 'my_dataviz'
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// Create a color scale
var color = d3.scaleOrdinal()
  .domain(data.map(d => d.name))
  .range(d3.schemeSet3);

// Compute the position of each group on the pie:
var pie = d3.pie()
  .value(d => d.value)
  .sort(null); // Do not sort group by size

// Shape helper to build arcs:
var arcGenerator = d3.arc()
  .innerRadius(0)
  .outerRadius(radius);

// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
svg
  .selectAll('mySlices')
  .data(pie(data))
  .enter()
  .append('path')
    .attr('d', arcGenerator)
    .attr('fill', d => color(d.data.name))
    .attr("stroke", "black")
    .style("stroke-width", "2px")
    .style("opacity", 0.7)

// Now add the annotation. Use the centroid method to get the best coordinates
svg
  .selectAll('mySlices')
  .data(pie(data))
  .enter()
  .append('text')
  .text(d => d.data.name)
  .attr("transform", d => "translate(" + arcGenerator.centroid(d) + ")")
  .style("text-anchor", "middle")
  .style("font-size", 17)
```

The code above produces a pie chart with labels as shown below:

![Pie Chart with Labels](https://raw.githubusercontent.com/d3/d3-3.x-api-reference/master/img/pie.png)

The code consists of the following parts:

1. An array of objects with data, which is used to generate the chart.
2. Setting the dimensions and margins of the chart.
3. Creating a color scale.
4. Computing the position of each group on the pie.
5. Creating a shape helper to build arcs.
6. Building the pie chart using the arc function.
7. Adding the annotation.

For more information on creating pie charts with d3.js, check out the [d3.js documentation](https://github.com/d3/d3-3.x-api-reference/blob/master/API-Reference.md#pie-d3-layout-pie).

onelinerhub: [How do I create a pie chart with labels using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-pie-chart-with-labels-using-d--js)