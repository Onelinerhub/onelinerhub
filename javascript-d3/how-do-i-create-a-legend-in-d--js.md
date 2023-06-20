# How do I create a legend in d3.js?
// plain

Creating a legend in d3.js is an easy task. To create a legend, you can use the `d3.legend` function. This function takes an array of data objects and creates a legend based on the data.

Below is an example of how to create a legend in d3.js, using a simple array of data objects:

```javascript
// Create data array
var data = [
  {name: 'Apple', color: '#FF0000'},
  {name: 'Orange', color: '#FFA500'},
  {name: 'Banana', color: '#FFFF00'}
];

// Create the legend
var legend = d3.legend()
  .data(data)
  .label('Fruit')
  .scale(d3.scaleOrdinal()
    .domain(data.map(function(d) { return d.name; }))
    .range(data.map(function(d) { return d.color; }))
  );

// Add the legend to the SVG
d3.select('svg')
  .append('g')
  .attr('class', 'legend')
  .call(legend);
```

This example will generate a legend with three entries, one for each item in the data array. Each entry will display the name of the fruit and its corresponding color.

The code consists of the following parts:

* Creation of the data array: This is an array of objects, each containing a name and a color.
* Creation of the legend: This is done using the `d3.legend` function, which takes an array of data objects and creates a legend based on the data.
* Adding the legend to the SVG: This is done by appending a `g` element to the SVG, setting its class to `legend`, and calling the `legend` function on it.

For more information, see the [d3.legend documentation](https://github.com/d3/d3-legend).

onelinerhub: [How do I create a legend in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-legend-in-d--js)