# &#24773;

How do I use d3.js to create a graph?
// plain

d3.js is a powerful JavaScript library for creating interactive data visualizations. It can be used to create a variety of charts and graphs, including bar charts, line graphs, and scatter plots. To create a graph using d3.js, you need to include the library in your HTML page, create a new SVG element, and define the data you want to visualize.

For example, the following code creates a simple bar chart using d3.js:

```
<!DOCTYPE html>
<html>
<head>
  <title>My Bar Chart</title>
  <script src="https://d3js.org/d3.v5.min.js"></script>
</head>
<body>
  <svg width="500" height="500"></svg>
  <script>
    // Set up our data
    var data = [4, 8, 15, 16, 23, 42];

    // Create our SVG element
    var svg = d3.select("svg");

    // Create our bars
    svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", function(d, i) {
        return i * 70;
      })
      .attr("y", function(d) {
        return 500 - d * 5;
      })
      .attr("width", 65)
      .attr("height", function(d) {
        return d * 5;
      })
      .attr("fill", "green");
  </script>
</body>
</html>
```

The code above will produce a bar chart like this:

![Bar Chart](https://miro.medium.com/max/700/1*_KpT-w5bvZxKUfVrv9SVng.png)

The code consists of several parts:

1. Include the d3.js library in the HTML page.
2. Create a new SVG element.
3. Define the data to be visualized.
4. Create the bars using the `svg.selectAll()` method.
5. Set the `x` and `y` attributes of the bars using the `attr()` method.
6. Set the `width`, `height`, and `fill` attributes of the bars using the `attr()` method.

For more information on creating charts and graphs with d3.js, see the following links:

- [D3.js Tutorials](https://d3js.org/#tutorials)
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Examples](https://bl.ocks.org/mbostock)

onelinerhub: [&#24773;

How do I use d3.js to create a graph?](https://onelinerhub.com/javascript-d3/----------how-do-i-use-d--js-to-create-a-graph)