# How can I create a flowchart using d3.js?
// plain

Creating a flowchart using d3.js is relatively simple.

First, you need to create the data structure that will be used to generate the chart. This data should be in the form of a hierarchical JSON object. For example:

```
var data = {
  "name": "Root Node",
  "children": [
    {
      "name": "Child Node 1"
    },
    {
      "name": "Child Node 2",
      "children": [
        {
          "name": "Grandchild Node 1"
        },
        {
          "name": "Grandchild Node 2"
        }
      ]
    }
  ]
};
```

Next, you need to create the SVG element and set its width and height.

```
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);
```

Then, you need to create a new tree layout and set the size.

```
var tree = d3.layout.tree()
    .size([width, height - 200]);
```

Next, you need to create the nodes and links.

```
var nodes = tree.nodes(data);
var links = tree.links(nodes);
```

Then, you need to draw the nodes and links on the SVG element.

```
var node = svg.selectAll(".node")
    .data(nodes)
    .enter().append("g")
    .attr("class", "node")
    .attr("transform", function(d) {
      return "translate(" + d.x + "," + d.y + ")";
    });

node.append("circle")
    .attr("r", 10);

node.append("text")
    .attr("dx", -3)
    .attr("dy", 3)
    .text(function(d) {
      return d.name;
    });

svg.selectAll(".link")
    .data(links)
    .enter().append("path")
    .attr("class", "link")
    .attr("d", diagonal);
```

Finally, you need to add styling to the nodes and links.

```
.node circle {
  fill: #fff;
  stroke: steelblue;
  stroke-width: 3px;
}

.node text {
  font: 12px sans-serif;
}

.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 2px;
}
```

This is how you can create a flowchart using d3.js.

## Code explanation
**

* `var data = {...}` - This is the data structure that will be used to generate the chart. It should be a hierarchical JSON object.
* `var svg = d3.select("body").append("svg")...` - This creates the SVG element and sets its width and height.
* `var tree = d3.layout.tree()...` - This creates a new tree layout and sets the size.
* `var nodes = tree.nodes(data);` - This creates the nodes from the data.
* `var links = tree.links(nodes);` - This creates the links between the nodes.
* `var node = svg.selectAll(".node")...` - This draws the nodes on the SVG element.
* `svg.selectAll(".link")...` - This draws the links on the SVG element.
* `.node circle {...}`, `.node text {...}`, `.link {...}` - This is styling for the nodes and links.

**## Helpful links**

* [D3.js Documentation](https://d3js.org/)
* [D3.js Tree Layout](https://github.com/d3/d3-hierarchy#tree)
* [D3.js Diagonal Paths](https://github.com/d3/d3-shape#diagonal)

onelinerhub: [How can I create a flowchart using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-flowchart-using-d--js)