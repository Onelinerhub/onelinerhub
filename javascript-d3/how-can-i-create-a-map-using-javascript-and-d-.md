# How can I create a map using JavaScript and D3?
// plain

Creating a map using JavaScript and D3 is relatively straightforward. Here is an example code block to get started:

```
var width = 960,
    height = 500;

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var g = svg.append("g");

d3.json("https://d3js.org/us-10m.v1.json", function(error, us) {
  if (error) throw error;

g.append("g")
    .attr("id", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter().append("path")
      .attr("d", d3.geoPath());

g.append("path")
    .attr("id", "state-borders")
    .attr("d", d3.geoPath(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; })));
});
```

## Code explanation


1. `var width = 960, height = 500` - This sets the width and height of the SVG element that will contain the map.
2. `var svg = d3.select("body").append("svg")` - This creates an SVG element and appends it to the body of the HTML page.
3. `var g = svg.append("g")` - This creates a group element in the SVG element.
4. `d3.json("https://d3js.org/us-10m.v1.json", function(error, us)` - This loads the TopoJSON data for the United States.
5. `g.append("g")` - This creates a new group element in the SVG element.
6. `.selectAll("path")` - This selects all the path elements in the group.
7. `.data(topojson.feature(us, us.objects.states).features)` - This binds the data to the path elements.
8. `.enter().append("path")` - This adds a path element for each data element.
9. `.attr("d", d3.geoPath())` - This sets the path's data attribute to the geographic path generator.

Here are some relevant links for further reading:

- [D3 Geo Paths](https://github.com/d3/d3-geo#geoPath)
- [D3 TopoJSON](https://github.com/topojson/topojson-client#api-reference)
- [D3 and Maps Tutorial](https://bost.ocks.org/mike/map/)

onelinerhub: [How can I create a map using JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-map-using-javascript-and-d-)