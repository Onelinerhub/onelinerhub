# How do I update the axis scale in d3.js?
// plain

Updating the axis scale in d3.js is a relatively simple process. The following example code will illustrate the process:

```
// Set up the SVG
var svg = d3.select("body").append("svg")
    .attr("width", 500)
    .attr("height", 500);

// Set up the x and y scales
var xScale = d3.scaleLinear()
    .domain([0, 10])
    .range([0, 500]);

var yScale = d3.scaleLinear()
    .domain([0, 10])
    .range([500, 0]);

// Draw the x and y axis
var xAxis = d3.axisBottom(xScale);
var yAxis = d3.axisLeft(yScale);
svg.append("g")
    .attr("transform", "translate(0," + 500 + ")")
    .call(xAxis);
svg.append("g")
    .call(yAxis);

// Update the x and y scales
xScale.domain([5, 10]);
yScale.domain([5, 10]);

// Update the x and y axis
svg.select(".x-axis")
    .transition()
    .call(xAxis);
svg.select(".y-axis")
    .transition()
    .call(yAxis);
```

This example code will produce a 500x500 SVG with the x and y axis drawn using the initial scales. Then the scales are updated and the axis are updated by selecting the class of the axis and calling the axis function again.

## Code explanation

1. Set up the SVG
2. Set up the x and y scales
3. Draw the x and y axis
4. Update the x and y scales
5. Update the x and y axis

## Helpful links
- [d3.js documentation](https://github.com/d3/d3/wiki)
- [d3.js Axis](https://github.com/d3/d3-axis)
- [d3.js Scales](https://github.com/d3/d3-scale)

onelinerhub: [How do I update the axis scale in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-update-the-axis-scale-in-d--js)