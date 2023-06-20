# How do I create a graph using D3.js?
// plain

Creating a graph using D3.js is a relatively simple process. To begin, you will need to include the D3 library in your HTML document.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Next, you will need to define your data. This can be done in the form of an array.

```
var data = [1,2,3,4,5];
```

Once you have your data, you will need to create an SVG element in your HTML document.

```
<svg></svg>
```

Using the D3 library, you can then bind your data to the SVG element and create a graph.

```
var svg = d3.select("svg");

var line = d3.line()
    .x(function(d,i) { return i*50; })
    .y(function(d) { return d*50; });

svg.append("path")
    .data([data])
    .attr("d", line)
    .attr("fill", "none")
    .attr("stroke", "blue")
    .attr("stroke-width", 2);
```

This code will create a line graph with a blue line and a stroke width of 2.

## Helpful links
* [D3.js Documentation](https://github.com/d3/d3/wiki)
* [Tutorials and Examples](https://www.d3-graph-gallery.com/)

onelinerhub: [How do I create a graph using D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-graph-using-d--js)