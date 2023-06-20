# How do I create a histogram using d3.js?
// plain

To create a histogram using d3.js, you need to follow the steps below:

1. Create an array of data to represent the histogram, for example:
```
var data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
```

2. Create a function to calculate the histogram, for example:
```
function histogram(data) {
  // calculate the histogram
}
```

3. Use the d3.layout.histogram() function to create a histogram layout, for example:
```
var histogramLayout = d3.layout.histogram()
  .bins(10)
  (data);
```

4. Create a SVG element using the d3.select() function, for example:
```
var svg = d3.select("body")
  .append("svg")
  .attr("width", 500)
  .attr("height", 500);
```

5. Create the bars of the histogram using the d3.selectAll() function, for example:
```
svg.selectAll("rect")
  .data(histogramLayout)
  .enter()
  .append("rect")
  .attr("x", function(d) { return d.x; })
  .attr("y", function(d) { return d.y; })
  .attr("width", function(d) { return d.dx; })
  .attr("height", function(d) { return d.y; });
```

6. Add labels to the histogram using the d3.selectAll() and d3.append() functions, for example:
```
svg.selectAll("text")
  .data(histogramLayout)
  .enter()
  .append("text")
  .attr("x", function(d) { return d.x; })
  .attr("y", function(d) { return d.y; })
  .text(function(d) { return d.y; });
```

7. Finally, render the histogram using the d3.select() function, for example:
```
d3.select("body")
  .append("svg")
  .attr("width", 500)
  .attr("height", 500)
  .selectAll("rect")
  .data(histogramLayout)
  .enter()
  .append("rect")
  .attr("x", function(d) { return d.x; })
  .attr("y", function(d) { return d.y; })
  .attr("width", function(d) { return d.dx; })
  .attr("height", function(d) { return d.y; })
  .selectAll("text")
  .data(histogramLayout)
  .enter()
  .append("text")
  .attr("x", function(d) { return d.x; })
  .attr("y", function(d) { return d.y; })
  .text(function(d) { return d.y; });
```

## Helpful links
- https://github.com/d3/d3-3.x-api-reference/blob/master/Layouts.md#histogram
- https://www.d3-graph-gallery.com/graph/histogram_basic.html

onelinerhub: [How do I create a histogram using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-histogram-using-d--js)