# How do I create a node graph using D3.js?
// plain

To create a node graph using D3.js, you will need to include the D3 library in your HTML. To do this, include the following script tag in the `<head>` of your HTML document:

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Then, create a `<div>` element in the `<body>` of your HTML document to contain the graph.

Next, create a JavaScript file to contain the code to create the graph. In this file, create a data array of the nodes that you want to include in the graph. Each node should have an `id` and `name` attribute. For example:

```
var data = [
  {id: 0, name: "Node 1"},
  {id: 1, name: "Node 2"},
  {id: 2, name: "Node 3"},
  {id: 3, name: "Node 4"}
];
```

Then, use the D3 library to create a force-directed graph with the data array. To do this, use the `d3.forceSimulation()` and `d3.forceLink()` methods to create the graph. For example:

```
var simulation = d3.forceSimulation(data)
  .force("link", d3.forceLink().id(function(d) { return d.id; }))
  .force("charge", d3.forceManyBody())
  .force("center", d3.forceCenter(width / 2, height / 2));
```

Finally, use the `d3.select()` method to select the div element from the HTML document, and use the `.append()` method to append the graph to the div.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [Force-Directed Graph Tutorial](https://bl.ocks.org/mbostock/4062045)

onelinerhub: [How do I create a node graph using D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-node-graph-using-d--js)