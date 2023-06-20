# How do I create an x and y axis using d3.js?
// plain

To create an x and y axis using d3.js, you can use the `axis` function. This function takes two parameters, the `scale` and the `orientation`. The `scale` is a function that maps data values to display values. The `orientation` is either `"bottom"`, `"top"`, `"left"` or `"right"` and determines which direction the axis is drawn.

```
// Create an x scale
var xScale = d3.scaleLinear()
  .domain([0, 10])
  .range([0, 500]);

// Create an x axis
var xAxis = d3.axisBottom(xScale);

// Create a y scale
var yScale = d3.scaleLinear()
  .domain([0, 10])
  .range([500, 0]);

// Create a y axis
var yAxis = d3.axisLeft(yScale);
```

The code above creates two scales and two axes. The x scale maps data values from 0 to 10 to display values from 0 to 500. The x axis is drawn in the bottom direction. The y scale maps data values from 0 to 10 to display values from 500 to 0. The y axis is drawn in the left direction.

## Code explanation


- `d3.scaleLinear()`: Creates a linear scale which maps data values to display values. It takes two parameters, `domain` and `range`. The `domain` is an array of two values that specify the minimum and maximum values of the data. The `range` is an array of two values that specify the minimum and maximum values of the display.
- `d3.axisBottom()`: Creates an x axis in the bottom direction. It takes one parameter, the `scale` which is a function that maps data values to display values.
- `d3.axisLeft()`: Creates a y axis in the left direction. It takes one parameter, the `scale` which is a function that maps data values to display values.

## Helpful links

- [D3 Scales](https://github.com/d3/d3-scale)
- [D3 Axes](https://github.com/d3/d3-axis)

onelinerhub: [How do I create an x and y axis using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-an-x-and-y-axis-using-d--js)