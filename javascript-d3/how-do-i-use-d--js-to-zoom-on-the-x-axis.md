# How do I use D3.js to zoom on the x-axis?
// plain

Using D3.js to zoom on the x-axis is a simple process. The following example code block shows how to implement zoom on the x-axis.

```
// Set up the scale and range for the x-axis
var x = d3.scaleLinear()
  .domain([0, 100])
  .range([0, width]);

// Set up the zoom behavior
var zoom = d3.zoom()
  .scaleExtent([1, 32])
  .translateExtent([[0, 0], [width, height]])
  .extent([[0, 0], [width, height]])
  .on("zoom", zoomed);

// Add the zoom behavior to the x-axis
svg.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + height + ")")
  .call(xAxis)
  .call(zoom);

// Define the zoomed function
function zoomed() {
  x.domain(d3.event.transform.rescaleX(x2).domain());
  svg.select(".x.axis").call(xAxis);
}
```

This code does the following:

1. Sets up the scale and range for the x-axis using the `d3.scaleLinear()` method.
2. Sets up the zoom behavior using the `d3.zoom()` method.
3. Adds the zoom behavior to the x-axis using the `call()` method.
4. Defines the `zoomed()` function which rescales the x-axis using the `d3.event.transform.rescaleX()` method.

For more information on how to use D3.js to zoom on the x-axis, see the following links:

- [D3.js Zooming](https://www.d3-graph-gallery.com/graph/interaction_zoom.html)
- [D3.js Zoom Behavior](https://github.com/d3/d3-zoom#zoom-behavior)
- [D3.js Zoom Events](https://github.com/d3/d3-zoom#zoom-events)

onelinerhub: [How do I use D3.js to zoom on the x-axis?](https://onelinerhub.com/javascript-d3/how-do-i-use-d--js-to-zoom-on-the-x-axis)