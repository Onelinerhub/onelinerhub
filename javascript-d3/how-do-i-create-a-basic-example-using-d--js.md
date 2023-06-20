# How do I create a basic example using d3.js?
// plain

Creating a basic example using d3.js is relatively straightforward. Here is a simple example that creates a scatter plot:

```
<html>
  <head>
    <script src="https://d3js.org/d3.v5.min.js"></script>
  </head>
  <body>
    <div id="chart"></div>
    <script>
      // Set the dimensions of the canvas / graph
      const margin = {top: 30, right: 20, bottom: 30, left: 50},
        width = 600 - margin.left - margin.right,
        height = 270 - margin.top - margin.bottom;

      // Set the ranges
      const x = d3.scaleLinear().range([0, width]);
      const y = d3.scaleLinear().range([height, 0]);

      // Define the axes
      const xAxis = d3.axisBottom(x);
      const yAxis = d3.axisLeft(y);

      // Define the line
      const valueline = d3.line()
        .x(function(d) { return x(d.x); })
        .y(function(d) { return y(d.y); });

      // Adds the svg canvas
      const svg = d3.select("#chart")
        .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
        .append("g")
          .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

      // Get the data
      const data = [
        {x: 10, y: 20},
        {x: 40, y: 60},
        {x: 80, y: 50},
        {x: 130, y: 80},
        {x: 200, y: 130},
        {x: 250, y: 10},
        {x: 300, y: 90}
      ];

      // Scale the range of the data
      x.domain(d3.extent(data, function(d) { return d.x; }));
      y.domain([0, d3.max(data, function(d) { return d.y; })]);

      // Add the valueline path.
      svg.append("path")
          .data([data])
          .attr("class", "line")
          .attr("d", valueline);

      // Add the X Axis
      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

      // Add the Y Axis
      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis);
    </script>
  </body>
</html>
```

This code will create a scatter plot with a line connecting the points. It begins by setting the dimensions of the canvas and the ranges of the x and y axes. It then defines the axes, creates a line connecting the points, and adds an svg canvas. Finally, it sets the domain of the data, adds the line path, and adds the x and y axes.

Parts of the code:

- Setting the dimensions of the canvas and the ranges of the x and y axes: `const margin = {top: 30, right: 20, bottom: 30, left: 50}, width = 600 - margin.left - margin.right, height = 270 - margin.top - margin.bottom;`
- Defining the axes: `const xAxis = d3.axisBottom(x); const yAxis = d3.axisLeft(y);`
- Defining the line: `const valueline = d3.line() .x(function(d) { return x(d.x); }) .y(function(d) { return y(d.y); });`
- Adding the svg canvas: `const svg = d3.select("#chart") .append("svg") .attr("width", width + margin.left + margin.right) .attr("height", height + margin.top + margin.bottom) .append("g") .attr("transform", "translate(" + margin.left + "," + margin.top + ")");`
- Setting the domain of the data: `x.domain(d3.extent(data, function(d) { return d.x; })); y.domain([0, d3.max(data, function(d) { return d.y; })]);`
- Adding the line path: `svg.append("path") .data([data]) .attr("class", "line") .attr("d", valueline);`
- Adding the x and y axes: `svg.append("g") .attr("class", "x axis") .attr("transform", "translate(0," + height + ")") .call(xAxis); svg.append("g") .attr("class", "y axis") .call(yAxis);`

## Helpful links

- [d3.js](https://d3js.org/)
- [Scatter Plot Tutorial](https://www.d3-graph-gallery.com/graph/scatter_basic.html)

onelinerhub: [How do I create a basic example using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-basic-example-using-d--js)