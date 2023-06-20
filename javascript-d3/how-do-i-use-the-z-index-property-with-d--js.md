# How do I use the z-index property with d3.js?
// plain

The z-index property in d3.js is used to control the stacking order of elements. Elements with a higher z-index are placed on top of elements with a lower z-index. For example, the following code block sets the z-index for a circle element to 10:

```
d3.select("circle")
  .style("z-index", 10);
```

The output of the example code is that the circle element will now have a z-index of 10.

The code block consists of the following parts:

* `d3.select("circle")` - This selects the circle element.
* `.style("z-index", 10)` - This sets the z-index of the circle element to 10.

For more information on the z-index property in d3.js, see the following links:

* [Z-Index in D3](https://www.dashingd3js.com/svg-z-index)
* [D3 API Reference](https://github.com/d3/d3-selection/blob/master/README.md#selection_style)

onelinerhub: [How do I use the z-index property with d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-z-index-property-with-d--js)