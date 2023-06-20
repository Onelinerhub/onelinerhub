# How do I create a zoomable line chart using d3.js?
// plain

Creating a zoomable line chart using d3.js is relatively straightforward. The following example code block will create a zoomable line chart:

```
// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
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

//Read the data
d3.csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered_comma.csv", function(data) {

// Add X axis --> it is a date format
var x = d3.scaleTime()
  .domain(d3.extent(data, function(d) { return d.date; }))
  .range([ 0, width ]);
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, d3.max(data, function(d) { return +d.value; })])
  .range([ height, 0 ]);
svg.append("g")
  .call(d3.axisLeft(y));

// Add the line
svg.append("path")
  .datum(data)
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 1.5)
  .attr("d", d3.line()
    .x(function(d) { return x(d.date) })
    .y(function(d) { return y(d.value) })
    )

// Add the zoom functionality
svg.call(d3.zoom()
    .scaleExtent([1, 8])  // This control how much you can zoom out
    .on("zoom", zoomed));

function zoomed() {
  // create new scale ojects based on event
  var new_xScale = d3.event.transform.rescaleX(x);
  var new_yScale = d3.event.transform.rescaleY(y);

  // update axes
  svg.select(".x-axis").call(d3.axisBottom(new_xScale));
  svg.select(".y-axis").call(d3.axisLeft(new_yScale));

  // update line
  svg.selectAll(".line")
    .attr("d", d3.line()
      .x(function(d) { return new_xScale(d.date) })
      .y(function(d) { return new_yScale(d.value) })
      )
}
```

This code will create a line chart with axes, that can be zoomed in and out. It is composed of the following parts:

1. Setting the dimensions and margins of the graph: `var margin = {top: 10, right: 30, bottom: 30, left: 60}, width = 460 - margin.left - margin.right, height = 400 - margin.top - margin.bottom;`
2. Appending the svg object to the body of the page: `var svg = d3.select("#my_dataviz").append("svg")`
3. Reading the data: `d3.csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered_comma.csv", function(data) {`
4. Adding the X axis: `var x = d3.scaleTime().domain(d3.extent(data, function(d) { return d.date; })).range([ 0, width ]); svg.append("g").attr("transform", "translate(0," + height + ")").call(d3.axisBottom(x));`
5. Adding the Y axis: `var y = d3.scaleLinear().domain([0, d3.max(data, function(d) { return +d.value; })]).range([ height, 0 ]); svg.append("g").call(d3.axisLeft(y));`
6. Adding the line: `svg.append("path").datum(data).attr("fill", "none").attr("stroke", "steelblue").attr("stroke-width", 1.5).attr("d", d3.line().x(function(d) { return x(d.date) }).y(function(d) { return y(d.value) }))`
7. Adding the zoom functionality: `svg.call(d3.zoom().scaleExtent([1, 8]).on("zoom", zoomed));`

This code will generate a zoomable line chart like this:

![Zoomable Line Chart](https://www.datanovia.com/en/wp-content/uploads/2019/07/d3-line-chart-zoom-datanovia.png)

## Helpful links
* [D3.js Documentation](https://github.com/d3/d3/wiki)
* [Zoomable Line Chart Tutorial](https://www.datanovia.com/en/blog/d3-zoomable-line-chart/)

onelinerhub: [How do I create a zoomable line chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-zoomable-line-chart-using-d--js)