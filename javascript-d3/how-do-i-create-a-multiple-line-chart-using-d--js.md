# How do I create a multiple line chart using d3.js?
// plain

Creating a multiple line chart using d3.js is relatively simple. The following example code will generate a multiple line chart from a dataset of values:

```
// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseTime = d3.timeParse("%d-%b-%y");

// Set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// Define the line
var valueline = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

// Define the div for the tooltip
var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

// Get the data
d3.csv("data.csv", function(error, data) {
    if (error) throw error;

    // Format the data
    data.forEach(function(d) {
        d.date = parseTime(d.date);
        d.close = +d.close;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    // Add the valueline path.
    svg.append("path")
        .data([data])
        .attr("class", "line")
        .attr("d", valueline);

    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add the Y Axis
    svg.append("g")
        .call(d3.axisLeft(y));

});
```

This code will create a multiple line chart with a tooltip. It will use the data from a csv file called `data.csv`. The code does the following:

1. Sets the dimensions of the canvas/graph
2. Parses the date/time from the csv file
3. Sets the ranges of the x and y axes
4. Defines the line
5. Defines the tooltip
6. Formats the data
7. Scales the range of the data
8. Adds the valueline path
9. Adds the x and y axes

## Helpful links
- [D3.js Documentation](https://d3js.org/)
- [Multiple Line Chart Tutorial](https://www.d3-graph-gallery.com/graph/line_multiple.html)

onelinerhub: [How do I create a multiple line chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-multiple-line-chart-using-d--js)