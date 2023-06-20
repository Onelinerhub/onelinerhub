# visualization

How do I create an HTML visualization using D3.js?
// plain

Creating an HTML visualization using D3.js is a simple process. First, include the library in an HTML file, such as:
```
<script src="https://d3js.org/d3.v5.min.js"></script>
```
Then, create a `<svg>` element in the HTML page to contain the visualization:
```
<svg width="400" height="200"></svg>
```
The data for the visualization is usually stored in an array. For example, an array of numbers:
```
var data = [10, 20, 30, 40, 50];
```
The visualization is created using the `d3.select` method. This method takes the `<svg>` element and binds the data to it. For example:
```
d3.select("svg")
  .selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("width", 20)
  .attr("height", function(d) {
    return d;
  });
```
The code above will create a rectangle for each number in the data array, with the height of the rectangle equal to the corresponding number.

The parts of the code above are as follows:
- `d3.select("svg")`: selects the `<svg>` element to bind the data to.
- `.selectAll("rect")`: selects all the `<rect>` elements, which don't exist yet.
- `.data(data)`: binds the data array to the selection.
- `.enter()`: creates a place for the data to enter into the selection.
- `.append("rect")`: creates a `<rect>` element for each data point.
- `.attr("width", 20)`: sets the width of the rectangles to 20 pixels.
- `.attr("height", function(d) { return d; })`: sets the height of the rectangles to the corresponding data point.

The output of this code is a series of rectangles with the height equal to the corresponding number in the data array.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Tutorials](https://www.dashingd3js.com/table-of-contents)

onelinerhub: [visualization

How do I create an HTML visualization using D3.js?](https://onelinerhub.com/javascript-d3/visualization--how-do-i-create-an-html-visualization-using-d--js)