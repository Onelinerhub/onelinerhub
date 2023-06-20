# How do I create a heatmap using JavaScript and D3?
// plain

Creating a heatmap using JavaScript and D3 is a fairly straightforward process.

First, you'll need to include the necessary libraries. This includes D3.js, as well as a color scale. For this example, we'll be using d3-scale-chromatic.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://d3js.org/d3-scale-chromatic.v1.min.js"></script>
```

Next, you'll need to create the SVG element and set its width and height.

```
var svg = d3.select("body")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);
```

After that, you'll need to create the color scale. This scale will be used to assign a color to each cell in the heatmap.

```
var colorScale = d3.scaleSequential(d3.interpolateReds)
                   .domain([1, 10]);
```

Then, you'll need to create the data array and draw the rectangles that will make up the heatmap.

```
var data = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

svg.selectAll("rect")
   .data(data)
   .enter()
   .append("rect")
   .attr("x", function(d, i) {
     return i * 50;
   })
   .attr("y", function(d, i) {
     return i * 50;
   })
   .attr("width", 50)
   .attr("height", 50)
   .style("fill", function(d) {
     return colorScale(d);
   });
```

Finally, you'll need to add some styling to make the heatmap look presentable.

```
svg.selectAll("rect")
   .attr("stroke", "black")
   .attr("stroke-width", 1);
```

The result should look something like this:

![Heatmap](https://raw.githubusercontent.com/d3/d3-scale-chromatic/master/img/heatmap.png)

For more information, you can check out the [d3-scale-chromatic](https://github.com/d3/d3-scale-chromatic) and [d3.js](https://d3js.org/) documentation.

onelinerhub: [How do I create a heatmap using JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-heatmap-using-javascript-and-d-)