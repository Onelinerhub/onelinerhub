# How do I create a line plot using JavaScript and D3?
// plain

Creating a line plot using JavaScript and D3 is easy and straightforward. The following example code block will create a line plot from an array of data.

```
var data = [1, 2, 3, 4, 5];

var margin = {top: 20, right: 20, bottom: 20, left: 20},
    width = 420 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

var x = d3.scaleLinear()
    .domain([0, data.length - 1])
    .range([0, width]);

var y = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([height, 0]);

var line = d3.line()
    .x(function(d, i) { return x(i); })
    .y(function(d) { return y(d); });

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

svg.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(y));

svg.append("path")
    .datum(data)
    .attr("class", "line")
    .attr("d", line);
```

This code will create a line plot with the given data.

The code can be broken down into parts as follows:

1. Defining the size of the plot: This is done by setting the margins, width and height of the plot.
2. Scaling the data: This is done by using the `d3.scaleLinear()` function to map the data to the plot size.
3. Generating the line: This is done by using the `d3.line()` function to generate the line from the data.
4. Creating the SVG element: This is done by using the `d3.select()` function to create the SVG element and append it to the DOM.
5. Adding axes: This is done by using the `d3.axisBottom()` and `d3.axisLeft()` functions to add the axes to the plot.
6. Adding the line: This is done by using the `d3.append()` function to append the line to the SVG element.

This code will produce the following output:

![Line Plot Example](https://raw.githubusercontent.com/d3/d3-hierarchy/master/img/line-plot.png)

For more information on creating line plots with D3, see the following links:

- [D3 Line Chart Tutorial](https://www.d3-graph-gallery.com/line_chart.html)
- [D3 Line Chart Documentation](https://github.com/d3/d3-shape#lines)
- [D3 Line Chart Examples](https://observablehq.com/@d3/line-chart)

onelinerhub: [How do I create a line plot using JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-line-plot-using-javascript-and-d-)