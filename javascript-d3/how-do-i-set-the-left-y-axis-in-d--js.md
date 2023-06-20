# How do I set the left y-axis in d3.js?
// plain

Setting the left y-axis in d3.js can be done by using the `.axisLeft()` method. This method takes in an optional argument that specifies the scale for the axis. The following example code creates a linear scale and uses it to set the left y-axis:

```
//Create linear scale
var yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([0, 100]);

//Set left y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(yScale));
```

This code will create a left y-axis with a linear scale, ranging from 0 to 100.

The parts of the code are as follows:
* `d3.scaleLinear()`: creates a linear scale
* `.domain([0, 100])`: sets the lower and upper bounds of the scale
* `.range([0, 100])`: sets the range of the scale
* `svg.append("g")`: appends a group element to the SVG
* `.attr("class", "y axis")`: assigns the group element the class "y axis"
* `.call(d3.axisLeft(yScale))`: calls the axisLeft method and passes in the linear scale

## Helpful links
* [d3-axis](https://github.com/d3/d3-axis)
* [d3-scale](https://github.com/d3/d3-scale)

onelinerhub: [How do I set the left y-axis in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-set-the-left-y-axis-in-d--js)