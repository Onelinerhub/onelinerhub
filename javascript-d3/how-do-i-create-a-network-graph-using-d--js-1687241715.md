# How do I create a network graph using d3.js?
// plain

Creating a network graph using d3.js is a great way to visualize relationships between different data points. To do this, you will need to create a JavaScript file and include the d3.js library.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

You will also need to create a data structure that contains the nodes and links between them.

```
var data = {
  nodes: [
    {name: "node1"},
    {name: "node2"},
    {name: "node3"}
  ],
  links: [
    {source: 0, target: 1},
    {source: 1, target: 2}
  ]
}
```

Next, you will need to define the width and height of the graph and create a force simulation.

```
var width = 500;
var height = 500;

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.name; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));
```

You can then create SVG elements for the nodes and links, and bind the data to them.

```
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var link = svg.append("g")
    .attr("class", "links")
  .selectAll("line")
  .data(data.links)
  .enter().append("line")
    .attr("stroke-width", 2);

var node = svg.append("g")
    .attr("class", "nodes")
  .selectAll("circle")
  .data(data.nodes)
  .enter().append("circle")
    .attr("r", 10)
    .attr("fill", "red");
```

Finally, you can define the tick function and start the simulation.

```
simulation
    .nodes(data.nodes)
    .on("tick", ticked);

simulation.force("link")
    .links(data.links);

function ticked() {
  link
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  node
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
}
```

This will create a network graph with three nodes connected by two links.

## Helpful links
- [d3.js](https://d3js.org/)
- [Force Directed Graphs](https://bl.ocks.org/mbostock/4062045)

onelinerhub: [How do I create a network graph using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-network-graph-using-d--js-1687241715)