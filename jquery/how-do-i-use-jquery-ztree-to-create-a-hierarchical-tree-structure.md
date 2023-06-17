# How do I use jQuery ZTree to create a hierarchical tree structure?
// plain

jQuery ZTree is a plugin that can be used to create a hierarchical tree structure. It uses the HTML UL and LI tags to create a tree structure.

To use jQuery ZTree, include the jQuery library and the ZTree plugin in your HTML page.

```
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="http://ztree.me/v3/js/jquery.ztree.all-3.5.min.js"></script>
```

Then, create an HTML UL element and assign it an id.

```
<ul id="tree"></ul>
```

Next, create a JavaScript object containing the data for the tree.

```
var data = [
  {
    name: "Node 1",
    children: [
      { name: "Node 1.1" },
      { name: "Node 1.2" }
    ]
  },
  {
    name: "Node 2",
    children: [
      { name: "Node 2.1" },
      { name: "Node 2.2" }
    ]
  }
];
```

Finally, call the jQuery ZTree plugin to create the tree.

```
$("#tree").zTree({
  data: data
});
```

This will create a hierarchical tree structure using the data provided.

## Helpful links
- [jQuery ZTree plugin](https://www.ztree.me/)
- [jQuery ZTree API Documentation](https://www.ztree.me/v3/api.php)

onelinerhub: [How do I use jQuery ZTree to create a hierarchical tree structure?](https://onelinerhub.com/jquery/how-do-i-use-jquery-ztree-to-create-a-hierarchical-tree-structure)