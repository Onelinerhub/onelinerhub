# How do I create a gauge using d3.js?
// plain

Creating a gauge using d3.js is a straightforward process. The following example code block creates a simple gauge with a current value of 50 and a maximum value of 100:

```
var gauge = d3.select("#gauge")
    .append("svg")
    .attr("width", 200)
    .attr("height", 200);

var radius = Math.min(200, 200) / 2;

var arc = d3.arc()
    .innerRadius(radius - 25)
    .outerRadius(radius);

var pie = d3.pie()
    .value(function(d) { return d; })
    .sort(null);

var data = [50, 100 - 50];

var arcs = gauge.selectAll("g.arc")
    .data(pie(data))
    .enter()
    .append("g")
    .attr("class", "arc")
    .attr("transform", "translate(" + radius + "," + radius + ")");

arcs.append("path")
    .attr("fill", "#e8e8e8")
    .attr("d", arc);

arcs.append("path")
    .attr("fill", "#00bfff")
    .attr("d", arc);
```

This code will create a gauge with a current value of 50 and a maximum value of 100. The code consists of the following parts:

1. Select the container element and create an SVG element: `var gauge = d3.select("#gauge") .append("svg") .attr("width", 200) .attr("height", 200);`
2. Set the radius of the gauge: `var radius = Math.min(200, 200) / 2;`
3. Create an arc generator function: `var arc = d3.arc() .innerRadius(radius - 25) .outerRadius(radius);`
4. Create a pie generator function: `var pie = d3.pie() .value(function(d) { return d; }) .sort(null);`
5. Set the data for the gauge: `var data = [50, 100 - 50];`
6. Select all elements with class "arc" and bind the data: `var arcs = gauge.selectAll("g.arc") .data(pie(data)) .enter() .append("g") .attr("class", "arc") .attr("transform", "translate(" + radius + "," + radius + ")");`
7. Append two paths to the arcs to create the background and foreground of the gauge:
```
arcs.append("path")
    .attr("fill", "#e8e8e8")
    .attr("d", arc);

arcs.append("path")
    .attr("fill", "#00bfff")
    .attr("d", arc);
```

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [Creating a Gauge with D3.js](https://www.d3-graph-gallery.com/graph/gauge_basic.html)

onelinerhub: [How do I create a gauge using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-gauge-using-d--js)