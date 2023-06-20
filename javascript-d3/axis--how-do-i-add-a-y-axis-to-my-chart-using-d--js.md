# axis

How do I add a y-axis to my chart using d3.js?
// plain

Using d3.js, you can add a y-axis to your chart by first creating a scale and then creating an axis object.

First, create a scale using the d3.scaleLinear() method. This method takes two parameters: the domain (the range of data values) and the range (the range of values to be output). For example:

```
var yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([0, 500]);
```

This example creates a scale that takes a domain of values from 0 to 100 and maps them to a range of values from 0 to 500.

Next, create an axis object using the d3.axisLeft() method. This method takes one parameter, the scale you created in the previous step. For example:

```
var yAxis = d3.axisLeft(yScale);
```

Finally, add the axis to your chart by calling the .call() method on the axis object. This method takes one parameter, the selection of the chart you want to add the axis to. For example:

```
d3.select("#chart").call(yAxis);
```

This example adds the y-axis to the chart with the ID of "chart".

## Helpful links
- [d3.scaleLinear()](https://github.com/d3/d3-scale#scaleLinear)
- [d3.axisLeft()](https://github.com/d3/d3-axis#axisLeft)

onelinerhub: [axis

How do I add a y-axis to my chart using d3.js?](https://onelinerhub.com/javascript-d3/axis--how-do-i-add-a-y-axis-to-my-chart-using-d--js)