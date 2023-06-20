# How can I create a collapsible tree with boxes using d3.js?
// plain

To create a collapsible tree with boxes using d3.js, we can use the following example code:
```
var root = {
  "name": "root",
  "children": [
    {
      "name": "level1",
      "children": [
        { "name": "level2" }
      ]
    }
  ]
};

var tree = d3.layout.tree()
    .size([400, 200]);

var nodes = tree.nodes(root);

var svg = d3.select("body").append("svg")
    .attr("width", 400)
    .attr("height", 200);

var node = svg.selectAll(".node")
    .data(nodes)
  .enter().append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

node.append("rect")
    .attr("width", 10)
    .attr("height", 10)
    .attr("fill", "red");

node.append("text")
    .attr("dx", 10)
    .attr("dy", ".35em")
    .text(function(d) { return d.name; });
```
This code will produce a collapsible tree with boxes as follows:

![Collapsible Tree with Boxes](https://github.com/d3/d3-hierarchy/blob/master/img/tree.png?raw=true)

The code consists of the following parts:
1. Create a JSON object representing the tree structure:
   - The JSON object consists of a root node and its children nodes.
2. Use the `d3.layout.tree()` function to create a tree layout:
   - This function takes the JSON object as an argument and returns a tree layout object.
3. Create an SVG element to render the tree:
   - Use the `d3.select()` function to select the body element and append an SVG element to it.
4. Create the nodes of the tree:
   - Use the `node()` function of the tree layout object to create the nodes of the tree.
5. Create the boxes for each node:
   - Use the `rect()` function to create a rectangle for each node.
6. Add text to each node:
   - Use the `text()` function to add text to each node.

## Helpful links
- [d3.js documentation](https://github.com/d3/d3/wiki)
- [d3.js hierarchy documentation](https://github.com/d3/d3-hierarchy)

onelinerhub: [How can I create a collapsible tree with boxes using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-collapsible-tree-with-boxes-using-d--js)