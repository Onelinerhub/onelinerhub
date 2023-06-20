# How can I create a mindmap using d3.js?
// plain

A mindmap using d3.js can be created by following the steps below:

1. Create an SVG element to contain the mindmap.
```
var svg = d3.select("body").append("svg")
  .attr("width", 500)
  .attr("height", 500);
```

2. Create a hierarchical tree layout.
```
var tree = d3.tree()
  .size([500, 500]);
```

3. Create a data object to represent the mindmap.
```
var data = {
  "name": "Root",
  "children": [
    {
      "name": "Child 1"
    },
    {
      "name": "Child 2",
      "children": [
        {
          "name": "Grandchild 1"
        },
        {
          "name": "Grandchild 2"
        }
      ]
    }
  ]
};
```

4. Create a data object to represent the mindmap.
```
var nodes = tree(data);
```

5. Add nodes and links to the SVG element.
```
var link = svg.selectAll(".link")
  .data(nodes.links())
  .enter()
  .append("path")
  .attr("class", "link")
  .attr("d", d3.linkHorizontal()
    .x(function(d) { return d.y; })
    .y(function(d) { return d.x; }));

var node = svg.selectAll(".node")
  .data(nodes.descendants())
  .enter()
  .append("g")
  .attr("class", function(d) {
    return "node" +
      (d.children ? " node--internal" : " node--leaf"); })
  .attr("transform", function(d) {
    return "translate(" + d.y + "," + d.x + ")"; });

node.append("circle")
  .attr("r", 10);

node.append("text")
  .attr("dy", 3)
  .attr("x", function(d) { return d.children ? -8 : 8; })
  .style("text-anchor", function(d) {
    return d.children ? "end" : "start"; })
  .text(function(d) { return d.data.name; });
```

6. Output the mindmap.
```
<svg width="500" height="500">
  <path class="link" d="M0,100H200V0H100"></path>
  <g class="node node--internal" transform="translate(100,0)">
    <circle r="10"></circle>
    <text dy="3" x="-8">Root</text>
  </g>
  <g class="node node--internal" transform="translate(100,100)">
    <circle r="10"></circle>
    <text dy="3" x="-8">Child 1</text>
  </g>
  <g class="node node--internal" transform="translate(300,100)">
    <circle r="10"></circle>
    <text dy="3" x="-8">Child 2</text>
  </g>
  <g class="node node--leaf" transform="translate(200,200)">
    <circle r="10"></circle>
    <text dy="3" x="8">Grandchild 1</text>
  </g>
  <g class="node node--leaf" transform="translate(400,200)">
    <circle r="10"></circle>
    <text dy="3" x="8">Grandchild 2</text>
  </g>
</svg>
```

## Helpful links
- [d3.js documentation](https://github.com/d3/d3/blob/master/API.md)
- [d3.js tree layout](https://github.com/d3/d3-hierarchy/blob/master/README.md#tree)
- [d3.js link generator](https://github.com/d3/d3-shape/blob/master/README.md#links)

onelinerhub: [How can I create a mindmap using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-mindmap-using-d--js)