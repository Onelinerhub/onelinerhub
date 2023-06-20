# visualization

How can I create a network visualization using d3.js?
// plain

Using d3.js, you can create a network visualization by creating a force-directed graph. This graph will represent the relationships between nodes in a network. To create the graph, you will need to create a data set that contains the nodes and their relationships.

```
// Create the data set
var data = {
  "nodes": [
    { "name": "node1" },
    { "name": "node2" },
    { "name": "node3" }
  ],
  "links": [
    { "source": 0, "target": 1 },
    { "source": 1, "target": 2 }
  ]
};

// Create the force-directed graph
var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

var link = svg.append("g")
    .attr("class", "links")
  .selectAll("line")
  .data(data.links)
  .enter().append("line")
    .attr("stroke-width", 2)
    .attr("stroke", "#999");

var node = svg.append("g")
    .attr("class", "nodes")
  .selectAll("circle")
  .data(data.nodes)
  .enter().append("circle")
    .attr("r", 5)
    .attr("fill", function(d) { return color(d.group); })
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

node.append("title")
    .text(function(d) { return d.name; });

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

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
```

The code above will generate a force-directed graph of the relationships between the nodes in the data set. The nodes are represented by circles and the links between them are represented by lines. The code includes functions to handle dragging and dropping of the nodes, as well as a function to handle the animation of the graph.

The code consists of the following parts:

1. Create the data set: this part of the code defines the nodes and the links between them.
2. Create the force-directed graph: this part of the code creates the graph by setting the width and height of the SVG element, setting the colors for the nodes, and creating the force simulation.
3. Create the nodes and links: this part of the code creates the nodes and links and adds them to the graph.
4. Handle the animation: this part of the code handles the animation of the graph by updating the positions of the nodes and links on each tick.
5. Handle dragging and dropping: this part of the code handles dragging and dropping of the nodes by setting the x and y coordinates of the nodes when the drag is started, dragged, and ended.

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [Force-Directed Graph Tutorial](https://bl.ocks.org/mbostock/4062045)

onelinerhub: [visualization

How can I create a network visualization using d3.js?](https://onelinerhub.com/javascript-d3/visualization--how-can-i-create-a-network-visualization-using-d--js)