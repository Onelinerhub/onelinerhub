# How do I use the yscale feature in d3.js?
// plain

The `yscale` feature in d3.js is used to create a linear or logarithmic scale for the y-axis of a graph. This scale can be used to map data points to a given range of values on the y-axis.

The following example code creates a linear scale using `d3.scaleLinear()`:

```
var yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([0, 10]);
```

The `.domain()` function defines the range of values that the data points can take, and the `.range()` function defines the range of values that the y-axis should display. In this example, the data points can take values from 0 to 100, and the y-axis will display values from 0 to 10.

The scale can then be used to map data points to the y-axis. For example:

```
var yValue = yScale(50); // yValue = 5
```

In this example, the value 50 is mapped to the value 5 on the y-axis.

A logarithmic scale can be created using `d3.scaleLog()` instead of `d3.scaleLinear()`.

## Helpful links
- [d3-scale](https://github.com/d3/d3-scale)
- [d3-scaleLinear](https://github.com/d3/d3-scale#scaleLinear)
- [d3-scaleLog](https://github.com/d3/d3-scale#scaleLog)

onelinerhub: [How do I use the yscale feature in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-yscale-feature-in-d--js)