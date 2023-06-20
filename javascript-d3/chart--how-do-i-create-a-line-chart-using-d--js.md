# chart

How do I create a line chart using D3.js?
// plain

Creating a line chart using D3.js is a straightforward process. The following example code will produce a basic line chart:

```
// Create svg element
var svg = d3.select("body")
  .append("svg")
  .attr("width", 500)
  .attr("height", 300);

// Create data set
var data = [1,2,3,4,5,6,7];

// Create line
var line = d3.line()
  .x(function(d,i) { return i * 50; })
  .y(function(d) { return d * 30; });

// Add line path
svg.append("path")
  .data([data])
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 2)
  .attr("d", line);
```

This code will produce a line chart with a width of 500px and a height of 300px. The data set is an array of numbers from 1 to 7. The x-axis is determined by multiplying the index of the data array by 50. The y-axis is determined by multiplying the data value by 30. The line is then added to the svg element with the "d" attribute set to the line variable. The line is given a fill of none and a stroke of steelblue with a stroke-width of 2.

## Code explanation

- `var svg = d3.select("body")` - This line creates a new svg element and appends it to the body of the HTML page.
- `.attr("width", 500)` - This line sets the width of the svg element to 500px.
- `.attr("height", 300)` - This line sets the height of the svg element to 300px.
- `var data = [1,2,3,4,5,6,7]` - This line creates an array of numbers from 1 to 7 to be used as the data set.
- `var line = d3.line()` - This line creates a new line variable.
- `.x(function(d,i) { return i * 50; })` - This line sets the x-axis of the line by multiplying the index of the data array by 50.
- `.y(function(d) { return d * 30; })` - This line sets the y-axis of the line by multiplying the data value by 30.
- `svg.append("path")` - This line adds a path element to the svg element.
- `.data([data])` - This line sets the data set for the path element to the array of numbers.
- `.attr("fill", "none")` - This line sets the fill of the path element to none.
- `.attr("stroke", "steelblue")` - This line sets the stroke of the path element to steelblue.
- `.attr("stroke-width", 2)` - This line sets the stroke-width of the path element to 2.
- `.attr("d", line)` - This line sets the "d" attribute of the path element to the line variable.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Line Chart Tutorial](https://www.tutorialsteacher.com/d3js/create-line-chart-using-d3js)

onelinerhub: [chart

How do I create a line chart using D3.js?](https://onelinerhub.com/javascript-d3/chart--how-do-i-create-a-line-chart-using-d--js)