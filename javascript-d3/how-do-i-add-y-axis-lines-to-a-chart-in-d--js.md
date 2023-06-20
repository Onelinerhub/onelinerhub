# How do I add y-axis lines to a chart in d3.js?
// plain

Adding y-axis lines to a chart in d3.js can be done by using the `axisLeft()` function. This function takes in an instance of the `scaleLinear()` function, which is used to map values from data to a given range. The code block below shows a basic example of adding a y-axis line to a chart.

```
// create scale
var yScale = d3.scaleLinear()
  .domain([0, 100])
  .range([height, 0]);

// create y-axis
var yAxis = d3.axisLeft(yScale);

// add y-axis to chart
chart.append("g")
  .attr("class", "axis y")
  .call(yAxis);
```

This code will create a y-axis line with the given scale and add it to the chart. The `axisLeft()` function will create a vertical line with tick marks and labels. The `domain` of the `scaleLinear()` function is used to set the range of data values that will be mapped to the y-axis, and the `range` is used to set the range of pixel values that will be used to draw the y-axis.

## Code explanation


- `var yScale = d3.scaleLinear()`: creates an instance of the `scaleLinear()` function.
- `.domain([0, 100])`: sets the range of data values that will be mapped to the y-axis.
- `.range([height, 0])`: sets the range of pixel values that will be used to draw the y-axis.
- `var yAxis = d3.axisLeft(yScale)`: creates an instance of the `axisLeft()` function and passes in the `yScale` instance.
- `chart.append("g")`: adds a group element to the chart.
- `.attr("class", "axis y")`: sets the class of the group element to `axis y`.
- `.call(yAxis)`: calls the `axisLeft()` function and draws the y-axis line.

For more information on creating charts with d3.js, see the following links:

- [d3.js documentation](https://github.com/d3/d3/wiki)
- [d3.js tutorial](https://alignedleft.com/tutorials/d3)

onelinerhub: [How do I add y-axis lines to a chart in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-add-y-axis-lines-to-a-chart-in-d--js)