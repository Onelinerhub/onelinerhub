# How can I create a family tree using d3.js?
// plain

Creating a family tree using d3.js is possible by using the hierarchical edge bundling technique. This technique is used to visualize the relationships between nodes in a hierarchical structure. To create a family tree, you will need to create a data structure that contains the relationships between family members. This data can then be passed to the d3.js library to create the visualization.

## Example code

```
// data structure containing family relationships
var familyTreeData = {
  name: "John Doe",
  children: [
    {
      name: "Jane Doe",
      children: [
        { name: "Jimmy Doe" },
        { name: "Jill Doe" }
      ]
    },
    {
      name: "Jim Doe",
      children: [
        { name: "Jack Doe" },
        { name: "Jill Doe" }
      ]
    }
  ]
};

// Create the visualization using d3.js
var familyTree = d3.hierarchy(familyTreeData);

// Output
No output
```

The code above creates a data structure that contains the relationships between family members. This data is then passed to the d3.js library to create the visualization. The hierarchical edge bundling technique is used to create the family tree visualization.

Parts of the code:

- `var familyTreeData`: This is the data structure containing the family relationships.
- `d3.hierarchy(familyTreeData)`: This is the function used to create the visualization from the data structure.

## Helpful links

- [Hierarchical Edge Bundling](https://bl.ocks.org/mbostock/7607999)
- [d3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How can I create a family tree using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-family-tree-using-d--js)