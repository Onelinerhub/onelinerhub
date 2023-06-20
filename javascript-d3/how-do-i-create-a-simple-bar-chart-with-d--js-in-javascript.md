# How do I create a simple bar chart with D3.js in JavaScript?
// plain

To create a simple bar chart with D3.js in JavaScript, you can use the following code example:

```
// set up svg canvas
var svg = d3.select("body")
    .append("svg")
    .attr("width", 500)
    .attr("height", 500);

// set up data
var dataset = [ 5, 10, 15, 20, 25 ];

// set up scales
var xScale = d3.scaleBand()
    .domain(d3.range(dataset.length))
    .rangeRound([0, 500])
    .paddingInner(0.05);

var yScale = d3.scaleLinear()
    .domain([0, d3.max(dataset)])
    .range([500, 0]);

// set up bars
svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("x", function(d, i) {
        return xScale(i);
    })
    .attr("y", function(d) {
        return yScale(d);
    })
    .attr("width", xScale.bandwidth())
    .attr("height", function(d) {
        return 500 - yScale(d);
    })
    .attr("fill", "teal");
```

This code will generate a simple bar chart like this:

![Simple Bar Chart](https://github.com/d3/d3-examples/raw/master/img/bar-simple.png)

The code consists of the following parts:

1. Setting up an SVG canvas to draw the chart on:
   - `var svg = d3.select("body").append("svg").attr("width", 500).attr("height", 500);`
2. Setting up the data to be used in the chart:
   - `var dataset = [ 5, 10, 15, 20, 25 ];`
3. Setting up the scales for the x and y axes:
   - `var xScale = d3.scaleBand().domain(d3.range(dataset.length)).rangeRound([0, 500]).paddingInner(0.05);`
   - `var yScale = d3.scaleLinear().domain([0, d3.max(dataset)]).range([500, 0]);`
4. Setting up the bars of the chart:
   - `svg.selectAll("rect").data(dataset).enter().append("rect")`
   - `.attr("x", function(d, i) { return xScale(i); })`
   - `.attr("y", function(d) { return yScale(d); })`
   - `.attr("width", xScale.bandwidth())`
   - `.attr("height", function(d) { return 500 - yScale(d); })`
   - `.attr("fill", "teal");`

For more information on how to create bar charts with D3.js, please see the following links:

- [D3 Bar Chart Tutorial](https://www.d3-graph-gallery.com/barplot.html)
- [D3 Bar Chart Documentation](https://github.com/d3/d3-shape/blob/master/README.md#bars)
- [D3 Scales Documentation](https://github.com/d3/d3-scale/blob/master/README.md)

onelinerhub: [How do I create a simple bar chart with D3.js in JavaScript?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-simple-bar-chart-with-d--js-in-javascript)