# How do I use d3.js to enable zooming and panning in my web application?
// plain

Using d3.js to enable zooming and panning in a web application is quite easy. The following example code block shows how to do it:

```
// set up zoom behaviour
var zoom = d3.zoom()
  .scaleExtent([1, 8])
  .on("zoom", zoomed);

// call the zoom behaviour on the svg element
svg.call(zoom);

// define the zoomed function
function zoomed() {
  // apply the transform to the elements
  g.attr("transform", d3.event.transform);
}
```

This code block will enable zooming and panning on an SVG element. The `scaleExtent` function defines the range of zoom levels that are allowed. The `zoomed` function defines the action that should be taken when the user zooms or pans. In this example, the `transform` attribute of the `g` element is set to the current transform.

## Helpful links
- [D3.js Zoom Behavior](https://github.com/d3/d3-zoom#zoom)
- [D3.js Transformations](https://github.com/d3/d3-transform#transform)

onelinerhub: [How do I use d3.js to enable zooming and panning in my web application?](https://onelinerhub.com/javascript-d3/how-do-i-use-d--js-to-enable-zooming-and-panning-in-my-web-application)