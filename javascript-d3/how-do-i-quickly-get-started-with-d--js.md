# How do I quickly get started with d3.js?
// plain

To quickly get started with d3.js, you need to include the d3.js library in your HTML page. This can be done by adding the following line of code to the `<head>` section of your HTML page:

```html
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Once the library is included, you can create a basic bar chart by writing the following code:

```js
// Set up the dimensions of the SVG
var width = 500;
var height = 500;

// Create an SVG element
var svg = d3.select("body")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

// Create a data array
var data = [10, 20, 30, 40, 50];

// Create a scale to map the data elements to the SVG
var x = d3.scaleBand()
  .domain(data)
  .range([0, width])
  .padding(0.2);

// Create a bar chart
svg.selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("x", function(d) {
    return x(d);
  })
  .attr("y", function(d) {
    return height - d;
  })
  .attr("width", x.bandwidth)
  .attr("height", function(d) {
    return d;
  })
  .attr("fill", "blue");
```

This code will create a basic bar chart with the data elements mapped to the SVG. The code consists of the following parts:

1. Setting up the dimensions of the SVG
2. Creating an SVG element
3. Creating a data array
4. Creating a scale to map the data elements to the SVG
5. Creating a bar chart

For more information on getting started with d3.js, please refer to the following links:

* [d3.js Documentation](https://github.com/d3/d3/wiki)
* [d3.js Tutorials](https://www.d3-graph-gallery.com/tutorials.html)
* [d3.js Examples](https://observablehq.com/@d3/gallery)

onelinerhub: [How do I quickly get started with d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-quickly-get-started-with-d--js)