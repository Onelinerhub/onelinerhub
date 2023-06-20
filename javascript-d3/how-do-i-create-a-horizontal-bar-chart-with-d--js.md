# How do I create a horizontal bar chart with D3.js?
// plain

Creating a horizontal bar chart with D3.js is relatively simple.

The following example code will create a basic horizontal bar chart with a few hardcoded data points:

```
<!DOCTYPE html>
<html>
<head>
  <title>D3 Horizontal Bar Chart Example</title>
  <script src="https://d3js.org/d3.v4.min.js"></script>
  <style>
    .bar {
      fill: steelblue;
    }
  </style>
</head>
<body>
  <svg width="400" height="200"></svg>
  <script>
    const svg = d3.select("svg");
    const data = [10, 20, 30, 40, 50];

    const xScale = d3.scaleLinear()
      .domain([0, d3.max(data)])
      .range([0, 400]);

    const yScale = d3.scaleLinear()
      .domain([0, data.length])
      .range([0, 200]);

    const bar = svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", 0)
      .attr("y", (d, i) => yScale(i))
      .attr("width", d => xScale(d))
      .attr("height", 20)
      .attr("class", "bar");
  </script>
</body>
</html>
```

The output of this code will be a horizontal bar chart with 5 bars, each bar representing the corresponding data point:

![alt text](https://i.imgur.com/9pTfFzH.png "Horizontal Bar Chart")

The code consists of the following sections:

1. **HTML boilerplate**: This includes the `<html>`, `<head>`, `<title>`, and `<style>` tags to set up the page.
2. **Load D3.js**: This includes the `<script>` tag to load the D3.js library.
3. **Create SVG element**: This includes the `<svg>` tag to create an SVG element to hold the chart.
4. **Set up data**: This includes an array of numbers to use as the data points for the chart.
5. **Create scales**: This includes two `scaleLinear()` functions to create an x-scale and a y-scale for the chart.
6. **Create bars**: This includes a `selectAll()` and `enter()` function to create the bars based on the data and the scales.

For more information on creating bar charts with D3.js, see the following links:

- [D3.js Bar Chart Tutorial](https://www.d3-graph-gallery.com/barplot.html)
- [D3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How do I create a horizontal bar chart with D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-horizontal-bar-chart-with-d--js)