# How do I create a histogram using d3.js?
// plain

Creating a histogram using d3.js is a relatively simple process. Here is an example of code that will create a basic histogram:

```
// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 40},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// X axis
var x = d3.scaleBand()
  .range([ 0, width ])
  .domain(data.map(function(d) { return d.name; }))
  .padding(0.2);
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x))
  .selectAll("text")
    .attr("transform", "translate(-10,0)rotate(-45)")
    .style("text-anchor", "end");

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, d3.max(data, function(d) { return +d.frequency; })])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y));

// Bars
svg.selectAll("mybar")
  .data(data)
  .enter()
  .append("rect")
    .attr("x", function(d) { return x(d.name); })
    .attr("y", function(d) { return y(d.frequency); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d.frequency); })
    .attr("fill", "#69b3a2")
```

This code will create a histogram with the following parts:

* Set the dimensions and margins of the graph: This part of the code establishes the size of the graph and the margins of the graph.
* Append the svg object to the body of the page: This part of the code creates an svg object and appends it to the page.
* X axis: This part of the code creates the x axis.
* Add Y axis: This part of the code creates the y axis.
* Bars: This part of the code creates the bars of the histogram.

Here is an example output of the code:

![alt text](https://i.imgur.com/JWO4dwv.png "Example Histogram Output")

## Helpful links

* [D3.js Documentation](https://github.com/d3/d3/wiki)
* [D3.js Tutorial](https://www.tutorialsteacher.com/d3js)
* [D3.js Histogram Tutorial](https://www.d3-graph-gallery.com/graph/histogram_basic.html)

onelinerhub: [How do I create a histogram using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-histogram-using-d--js-1687237256)