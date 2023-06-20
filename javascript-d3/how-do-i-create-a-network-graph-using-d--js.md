# How do I create a network graph using d3.js?
// plain

Creating a network graph using d3.js is relatively easy. The following example code block creates a network graph with 4 nodes and 5 links:

```
var nodes = [
  {id: 0, label: 'Node 0'},
  {id: 1, label: 'Node 1'},
  {id: 2, label: 'Node 2'},
  {id: 3, label: 'Node 3'}
];

var links = [
  {source: 0, target: 1},
  {source: 0, target: 2},
  {source: 0, target: 3},
  {source: 1, target: 2},
  {source: 2, target: 3}
];

var width = 500, height = 500;

var svg = d3.select("body").append("svg")
            .attr("width", width)
            .attr("height", height);

var force = d3.layout.force()
              .nodes(nodes)
              .links(links)
              .size([width, height])
              .linkDistance(150)
              .charge(-400);

force.start();

var link = svg.selectAll(".link")
              .data(links)
              .enter().append("line")
              .attr("class", "link");

var node = svg.selectAll(".node")
              .data(nodes)
              .enter().append("circle")
              .attr("class", "node")
              .attr("r", 10)
              .call(force.drag);

force.on("tick", function() {
  link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  node.attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
});
```

The code works as follows:
* `var nodes`: creates an array of objects containing the nodes of the graph, with an `id` and a `label`.
* `var links`: creates an array of objects containing the links between the nodes, with a `source` and a `target`.
* `var width` and `var height`: set the width and height of the graph.
* `var svg`: creates an SVG element in the DOM.
* `var force`: creates a force-directed graph layout.
* `var link`: creates a line element for each link in the graph.
* `var node`: creates a circle element for each node in the graph.
* `force.on("tick"`: updates the position of the nodes and links on each tick.

The output of the code is a network graph with 4 nodes and 5 links, as shown below:

![Network Graph](https://i.imgur.com/UuXs2lw.png)

## Helpful links
* [D3.js Docs](https://d3js.org/)
* [Force-Directed Graph Tutorial](https://bl.ocks.org/mbostock/4062045)

onelinerhub: [How do I create a network graph using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-network-graph-using-d--js)