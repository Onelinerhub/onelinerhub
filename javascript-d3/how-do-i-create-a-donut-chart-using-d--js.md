# How do I create a donut chart using d3.js?
// plain

A donut chart can be created using d3.js by following these steps:

1. Create an SVG element and set its width and height:
```
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);
```

2. Create a group element and set its transform attribute to position the donut chart:
```
var g = svg.append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
```

3. Create a color scale to use for the pie chart:
```
var color = d3.scaleOrdinal(d3.schemeCategory10);
```

4. Create a pie layout and set its size and value accessor:
```
var pie = d3.pie()
    .value(function(d) { return d.value; })
    .sort(null);
```

5. Create an arc generator and set its inner and outer radius:
```
var arc = d3.arc()
    .innerRadius(radius - donutWidth)
    .outerRadius(radius);
```

6. Create a path element and set its d attribute to the arc generator:
```
g.selectAll(".arc")
    .data(pie(data))
    .enter().append("path")
    .attr("d", arc)
    .style("fill", function(d) { return color(d.data.label); });
```

7. Add a label to the center of the donut chart:
```
var label = g.append("text")
    .attr("dy", ".35em")
    .style("text-anchor", "middle")
    .text(function(d) { return d.label; });
```

The output of this code will be a donut chart with a label in the center.

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Pie Chart Tutorial](https://www.d3-graph-gallery.com/graph/pie_basic.html)

onelinerhub: [How do I create a donut chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-donut-chart-using-d--js)