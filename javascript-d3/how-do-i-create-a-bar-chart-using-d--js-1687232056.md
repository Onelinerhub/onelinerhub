# How do I create a bar chart using d3.js?
// plain

To create a bar chart using d3.js, you will need to use the `.selectAll()` and `.data()` methods to bind your data to the chart, and then use the `.enter()` method to create the elements for the chart. You will then use the `.append()` method to create an SVG element for each bar, and the `.attr()` method to set the height and width of the bar. Finally, you will use the `.style()` method to set the color of the bar.

For example:

```
var data = [2, 5, 10, 20];

var svg = d3.select("body")
  .append("svg")
  .attr("width", 500)
  .attr("height", 500);

var bars = svg.selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("width", function(d) {
    return d * 10;
  })
  .attr("height", 50)
  .attr("y", function(d, i) {
    return i * 100;
  })
  .style("fill", "steelblue");
```

This code will create 4 bars, with a width of 2x10, 5x10, 10x10, and 20x10 respectively. The bars will have a height of 50 and the color will be steelblue.

## Code explanation


- `var data = [2, 5, 10, 20];`: This creates an array of data to be used in the chart.

- `var svg = d3.select("body")`: This selects the body of the HTML document.

- `.append("svg")`: This appends an SVG element to the body of the HTML document.

- `.attr("width", 500)`: This sets the width of the SVG element to 500.

- `.attr("height", 500)`: This sets the height of the SVG element to 500.

- `var bars = svg.selectAll("rect")`: This selects all the rectangles in the SVG element.

- `.data(data)`: This binds the data to the chart.

- `.enter()`: This creates the elements for the chart.

- `.append("rect")`: This appends a rectangle element to the SVG element.

- `.attr("width", function(d) { return d * 10; })`: This sets the width of the rectangle to the value of the data multiplied by 10.

- `.attr("height", 50)`: This sets the height of the rectangle to 50.

- `.attr("y", function(d, i) { return i * 100; })`: This sets the y position of the rectangle to the value of the data multiplied by 100.

- `.style("fill", "steelblue")`: This sets the color of the rectangle to steelblue.

## Helpful links

- [d3.js Documentation](https://github.com/d3/d3/wiki)
- [Tutorial: How to Make a Bar Chart with D3.js](https://www.digitalocean.com/community/tutorials/how-to-make-a-bar-chart-with-d3-js)

onelinerhub: [How do I create a bar chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-bar-chart-using-d--js-1687232056)