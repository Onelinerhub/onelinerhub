# How can I use D3 and JavaScript to create images?
// plain

Using D3 and JavaScript, you can create images by using SVG elements to draw shapes, text, and images. For example, the following code uses D3 to create a simple circle:

```
// Create a circle
var svg = d3.select("#container").append("svg")
  .attr("width", 100)
  .attr("height", 100);

var circle = svg.append("circle")
  .attr("cx", 50)
  .attr("cy", 50)
  .attr("r", 25)
  .style("fill", "purple");
```

This code would output an SVG circle element with a radius of 25, an x coordinate of 50, a y coordinate of 50, and a fill color of purple.

The code is composed of the following parts:

1. `d3.select("#container")`: Selects the HTML element with the id of "container"
2. `.append("svg")`: Appends an SVG element to the selected element
3. `.attr("width", 100)`: Sets the width of the SVG element to 100
4. `.attr("height", 100)`: Sets the height of the SVG element to 100
5. `.append("circle")`: Appends a circle element to the SVG element
6. `.attr("cx", 50)`: Sets the x coordinate of the circle element to 50
7. `.attr("cy", 50)`: Sets the y coordinate of the circle element to 50
8. `.attr("r", 25)`: Sets the radius of the circle element to 25
9. `.style("fill", "purple")`: Sets the fill color of the circle element to purple

You can also draw more complex shapes, text, and images with D3. For more information, see the [D3 documentation](https://github.com/d3/d3/wiki).

onelinerhub: [How can I use D3 and JavaScript to create images?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--and-javascript-to-create-images)