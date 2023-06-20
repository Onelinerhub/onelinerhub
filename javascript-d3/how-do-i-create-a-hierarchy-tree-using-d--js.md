# How do I create a hierarchy tree using d3.js?
// plain

Creating a hierarchy tree with d3.js is a relatively simple process. The following example code creates a basic tree structure from a JSON object:

```
// create a new tree
var tree = d3.tree();

// set the size of the tree
tree.size([500, 500]);

// create a JSON object with the tree data
var treeData = {
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

// create a selection from the tree
var treeRoot = d3.hierarchy(treeData);

// generate the tree
tree(treeRoot);

// append the tree to the DOM
d3.select('body').append('svg')
  .attr('width', 500)
  .attr('height', 500)
  .append('g')
  .attr('transform', 'translate(50,50)')
  .selectAll('g.node')
  .data(treeRoot.descendants())
  .enter()
  .append('g')
  .attr('transform', function(d) {
    return 'translate(' + d.x + ',' + d.y + ')';
  })
  .append('circle')
  .attr('r', 10);
```

This code will create an SVG element with a circle for each node in the tree. It makes use of the following parts of d3.js:

* `d3.tree` - creates a new tree layout.
* `tree.size` - sets the size of the tree.
* `d3.hierarchy` - creates a hierarchy object from the tree data.
* `tree` - generates the tree from the hierarchy object.
* `d3.select` - selects an element from the DOM.
* `attr` - sets attributes of a selection.
* `data` - binds data to a selection.
* `enter` - creates new elements for each data point.
* `append` - appends elements to a selection.

For more information on creating hierarchy trees with d3.js, see the [d3.js documentation](https://github.com/d3/d3-hierarchy#tree) and the [d3.js examples](https://observablehq.com/@d3/hierarchical-edge-bundling).

onelinerhub: [How do I create a hierarchy tree using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-hierarchy-tree-using-d--js)