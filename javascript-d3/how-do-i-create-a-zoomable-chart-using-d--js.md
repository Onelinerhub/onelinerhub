# How do I create a zoomable chart using d3.js?
// plain

Creating a zoomable chart with d3.js requires the following steps:

1. Create an SVG element in the HTML page to draw the chart.
```
<svg id="chart" width="900" height="500"></svg>
```

2. Create a margin object to position the chart within the SVG element.
```
var margin = {top: 20, right: 20, bottom: 30, left: 40};
```

3. Create a scale object to map the data to the chart area.
```
var x = d3.scaleLinear().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);
```

4. Create an axis object to draw the axes.
```
var xAxis = d3.axisBottom(x);
var yAxis = d3.axisLeft(y);
```

5. Create a zoom object to enable zooming.
```
var zoom = d3.zoom().on("zoom", zoomed);
```

6. Create a zoom function to update the chart when zooming.
```
function zoomed() {
  //update the x and y scale according to the zoom transform
  x.domain(d3.event.transform.rescaleX(xScale).domain());
  y.domain(d3.event.transform.rescaleY(yScale).domain());

  //redraw the axes
  svg.select(".x.axis").call(xAxis);
  svg.select(".y.axis").call(yAxis);

  //redraw the chart
  svg.selectAll(".bar")
    .attr("x", function(d) { return x(d.x); })
    .attr("y", function(d) { return y(d.y); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d.y); });
}
```

7. Finally, attach the zoom object to the SVG element.
```
svg.call(zoom);
```

## Helpful links
- [Zoomable Charts with D3.js](https://www.d3-graph-gallery.com/graph/interactivity_zoom.html)
- [D3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How do I create a zoomable chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-zoomable-chart-using-d--js)