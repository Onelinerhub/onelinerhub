# How can I create a bar chart using D3.js?
// plain

Creating a bar chart using D3.js is quite simple. The following example code will create a basic bar chart with a few bars.

```
// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// set the ranges
var x = d3.scaleBand()
          .range([0, width])
          .padding(0.1);
var y = d3.scaleLinear()
          .range([height, 0]);

// append the svg object to the body of the page
// append a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// get the data
d3.csv("data.csv", function(error, data) {
  if (error) throw error;

  // format the data
  data.forEach(function(d) {
    d.sales = +d.sales;
  });

  // Scale the range of the data in the domains
  x.domain(data.map(function(d) { return d.salesperson; }));
  y.domain([0, d3.max(data, function(d) { return d.sales; })]);

  // append the rectangles for the bar chart
  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.salesperson); })
      .attr("width", x.bandwidth())
      .attr("y", function(d) { return y(d.sales); })
      .attr("height", function(d) { return height - y(d.sales); });

});
```

This code will produce a bar chart with the following parts:

* `margin` - An object that contains the margins of the chart.
* `width` and `height` - Variables that contain the width and height of the chart.
* `x` and `y` - Scales that map the data to the chart.
* `svg` - An SVG element that will contain the chart.
* `data` - The data that will be used to create the chart.
* `x.domain` and `y.domain` - The domains of the x and y scales.
* `svg.selectAll` - Selects all elements that match the given selector.
* `.attr` - Sets the attributes of the selected elements.

The output of this code will be a bar chart with the data from the `data.csv` file.

## Helpful links

* [D3.js Documentation](https://d3js.org/)
* [D3.js Bar Chart Tutorial](https://www.d3-graph-gallery.com/barplot.html)

onelinerhub: [How can I create a bar chart using D3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-bar-chart-using-d--js)