# How do I create a horizontal bar chart using d3.js?
// plain

To create a horizontal bar chart using d3.js, you will need to use the `d3.scaleLinear()` and `d3.axisBottom()` functions.

You will also need to create an SVG element and append a group element to it.

Below is an example of a horizontal bar chart created with d3.js:

```javascript
// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%y").parse;

// Set the ranges
var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("data.csv", function(error, data) {
    data.forEach(function(d) {
        d.date = parseDate(d.date);
        d.close = +d.close;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

});
```

The code above will produce a horizontal bar chart with the following parts:

- `margin`: sets the dimensions of the canvas / graph
- `parseDate`: parses the date / time
- `x` and `y`: sets the ranges
- `xAxis` and `yAxis`: defines the axes
- `svg`: adds the SVG canvas
- `d3.csv()`: gets the data
- `x.domain()` and `y.domain()`: scales the range of the data
- `svg.append()`: adds the value line path
- `svg.append()`: adds the X axis
- `svg.append()`: adds the Y axis

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Tutorial](https://www.d3-graph-gallery.com/graph/barplot_horizontal.html)

onelinerhub: [How do I create a horizontal bar chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-horizontal-bar-chart-using-d--js)