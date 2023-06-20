# directed graph

How can I create a force directed graph using d3.js?
// plain

A force directed graph can be created using the d3.js library. This library provides a set of functions for creating and manipulating graphs. To create a force directed graph, the following code can be used:

```
// Create a force directed graph
var graph = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

// Add data to the graph
graph.nodes(nodes)
    .on("tick", ticked);

graph.force("link")
    .links(links);

// Draw the graph
var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
      .attr("r", 5)
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

// Update the graph with data
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

The code creates a force directed graph with nodes and links. It sets up the simulation with the `d3.forceSimulation()` function, which takes a set of forces as parameters. These forces define how the graph behaves. The `d3.forceLink()` force creates links between nodes, and the `d3.forceManyBody()` force creates repulsive forces between nodes. The `d3.forceCenter()` force keeps the graph centered in the viewport.

The data for the graph is added to the simulation with the `nodes()` and `links()` functions. The `tick()` function is called to update the graph with the new data. This function sets the positions of the nodes and links based on the forces in the simulation.

## Code explanation


* `d3.forceSimulation()` - Creates a force directed graph simulation, which takes a set of forces as parameters.
* `d3.forceLink()` - Creates links between nodes.
* `d3.forceManyBody()` - Creates repulsive forces between nodes.
* `d3.forceCenter()` - Keeps the graph centered in the viewport.
* `nodes()` - Adds data to the graph.
* `links()` - Adds data to the graph.
* `tick()` - Updates the graph with the new data.

## Helpful links

* [D3.js Documentation](https://github.com/d3/d3/wiki)
* [Force Directed Graph Tutorial](https://bl.ocks.org/mbostock/4062045)

onelinerhub: [directed graph

How can I create a force directed graph using d3.js?](https://onelinerhub.com/javascript-d3/directed-graph--how-can-i-create-a-force-directed-graph-using-d--js)