# How do I create a line graph with d3.js?
// plain

Creating a line graph with d3.js is a relatively simple task. Here is an example code block that will generate a basic line graph:

```
// set up the SVG
var svg = d3.select("body")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);

// set up the scales
var xScale = d3.scaleLinear()
               .domain([0, 10])
               .range([0, 500]);

var yScale = d3.scaleLinear()
               .domain([0, 10])
               .range([500, 0]);

// set up the line
var line = d3.line()
             .x(function(d) { return xScale(d.x); })
             .y(function(d) { return yScale(d.y); });

// create the line graph
svg.append("path")
   .datum(data)
   .attr("d", line)
   .attr("fill", "none")
   .attr("stroke", "blue")
   .attr("stroke-width", 2);
```

This code will generate a line graph with a blue line of width 2. The x and y scales are set up to accept data from 0 to 10 and the data is provided to the line generator which uses the scales to map the data to the SVG.

## Code explanation


* `svg` - sets up the SVG element that will contain the line graph
* `xScale` and `yScale` - set up the x and y scales to map the data points to the SVG
* `line` - set up the line generator to map the data points to the SVG
* `svg.append("path")` - creates the line graph in the SVG

Here are some helpful links for further reading:

* [D3.js Line Graph Tutorial](https://www.d3-graph-gallery.com/line.html)
* [D3.js Tutorials](https://www.d3-graph-gallery.com/tutorials.html)
* [D3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How do I create a line graph with d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-line-graph-with-d--js)