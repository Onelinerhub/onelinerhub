# How do I create a multiple line chart using D3.js?
// plain

Creating a multiple line chart using D3.js is a relatively simple process. The following example code will create a multi-line chart, using a dataset of three lines:

```
// set the dimensions and margins of the graph
var margin = {top: 20, right: 80, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%Y-%m-%d");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the line
var line1 = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.line1); });
var line2 = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.line2); });
var line3 = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.line3); });

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("data.csv", function(error, data) {
  if (error) throw error;

  // format the data
  data.forEach(function(d) {
      d.date = parseTime(d.date);
      d.line1 = +d.line1;
      d.line2 = +d.line2;
      d.line3 = +d.line3;
  });

  // Scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([
    d3.min(data, function(d) { return Math.min(d.line1, d.line2, d.line3); }),
    d3.max(data, function(d) { return Math.max(d.line1, d.line2, d.line3); })
  ]);

  // Add the line1 path.
  svg.append("path")
      .data([data])
      .attr("class", "line1")
      .attr("d", line1);

  // Add the line2 path.
  svg.append("path")
      .data([data])
      .attr("class", "line2")
      .attr("d", line2);

  // Add the line3 path.
  svg.append("path")
      .data([data])
      .attr("class", "line3")
      .attr("d", line3);

});
```

This code will create three SVG paths, each representing a line in the chart. The code consists of the following parts:

1. Setting the dimensions and margins of the graph.
2. Parsing the date/time data.
3. Setting the ranges for the x and y axes.
4. Defining the lines for each of the three datasets.
5. Appending the SVG object to the body of the page.
6. Reading in the data from a CSV file.
7. Formatting the data.
8. Scaling the range of the data.
9. Appending each of the three lines to the SVG object.

For more information on creating a multi-line chart with D3.js, see the following resources:

- [D3.js Multi-Line Chart Tutorial](https://www.d3-graph-gallery.com/graph/line_multiple.html)
- [D3.js Line Chart Tutorial](https://www.d3-graph-gallery.com/graph/line_basic.html)
- [D3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How do I create a multiple line chart using D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-multiple-line-chart-using-d--js-1687241102)