# How can I create a pie chart using D3 and JavaScript?
// plain

Creating a pie chart using D3 and JavaScript is a fairly straightforward process. The following example code will create a basic pie chart using the D3 library:

```javascript
// Set up the pie chart
var width = 500;
var height = 500;
var radius = Math.min(width, height) / 2;

// Create SVG element
var svg = d3.select("body")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g")
  .attr("transform", "translate(" + width/2 + "," + height/2 + ")");

// Create pie chart
var arc = d3.arc()
  .innerRadius(0)
  .outerRadius(radius);

var pie = d3.pie()
  .value(function(d) { return d.value; })(data);

var arcs = svg.selectAll("arc")
  .data(pie)
  .enter()
  .append("g")
  .attr("class", "arc");

arcs.append("path")
  .attr("fill", function(d, i) {
    return color(i);
  })
  .attr("d", arc);
```

This code will create a basic pie chart with the following parts:

1. A width and height variable that sets the size of the pie chart.
2. An SVG element which is used to contain the pie chart.
3. An arc element which defines the shape of the pie chart.
4. A pie element which defines the data used to create the pie chart.
5. An arcs element which is used to store the individual arcs that make up the pie chart.
6. A path element which is used to draw the individual arcs of the pie chart.

## Helpful links

- [D3 Pie Chart Tutorial](https://www.d3-graph-gallery.com/graph/pie_basic.html)
- [D3 Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How can I create a pie chart using D3 and JavaScript?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-pie-chart-using-d--and-javascript)