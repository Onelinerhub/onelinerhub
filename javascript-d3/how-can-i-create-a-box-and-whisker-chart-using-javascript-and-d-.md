# How can I create a box and whisker chart using JavaScript and D3?
// plain

A box and whisker chart can be created using JavaScript and D3 by following these steps:

1. Create a `svg` element to contain the chart:
```
var svg = d3.select("body")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
```

2. Create a `rect` element for each box and whisker:
```
svg.selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("x", function(d,i) {
    return xScale(i);
  })
  .attr("y", function(d) {
    return yScale(d.max);
  })
  .attr("height", function(d) {
    return yScale(d.min) - yScale(d.max);
  })
  .attr("width", xScale.bandwidth() )
  .attr("fill", "#69b3a2");
```

3. Create a `line` element for each box and whisker:
```
svg.selectAll("line")
  .data(data)
  .enter()
  .append("line")
  .attr("x1", function(d,i) {
    return xScale(i) + xScale.bandwidth()/2;
  })
  .attr("x2", function(d,i) {
    return xScale(i) + xScale.bandwidth()/2;
  })
  .attr("y1", function(d) {
    return yScale(d.min);
  })
  .attr("y2", function(d) {
    return yScale(d.max);
  })
  .attr("stroke", "black")
  .attr("stroke-width", 2);
```

4. Create a `circle` element to represent the median:
```
svg.selectAll("circle")
  .data(data)
  .enter()
  .append("circle")
  .attr("cx", function(d,i) {
    return xScale(i) + xScale.bandwidth()/2;
  })
  .attr("cy", function(d) {
    return yScale(d.median);
  })
  .attr("r", 4)
  .attr("fill", "black");
```

The output of this code would be a box and whisker chart with rectangles representing the box and whiskers, lines to connect the box and whiskers, and circles to represent the median.

## Helpful links
- [D3 Box and Whisker Chart Tutorial](https://www.d3-graph-gallery.com/boxplot.html)
- [D3 API Reference](https://github.com/d3/d3/blob/master/API.md)

onelinerhub: [How can I create a box and whisker chart using JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-box-and-whisker-chart-using-javascript-and-d-)