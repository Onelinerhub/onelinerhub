# How do I add x axis labels to a chart in d3.js?
// plain

To add x axis labels to a chart in d3.js, you will need to use the `axis` and `scale` functions.

First, you will need to define the scale of your x axis using the `scaleBand()` function. This function takes in the range of values of your x axis and returns a scale object.

```javascript
var xScale = d3.scaleBand()
  .range([0, width])
  .domain(data.map(function(d) { return d.x; }));
```

Next, you will need to create an x axis object using the `axisBottom()` function. This function takes in the scale object that you just created and returns an axis object.

```javascript
var xAxis = d3.axisBottom()
  .scale(xScale);
```

Finally, you will need to append the x axis object to your chart.

```javascript
svg.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + height + ")")
  .call(xAxis);
```

The above code will create an x axis with labels for the data points specified in the `data` array.

## Helpful links
- [d3-scale](https://github.com/d3/d3-scale)
- [d3-axis](https://github.com/d3/d3-axis)

onelinerhub: [How do I add x axis labels to a chart in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-add-x-axis-labels-to-a-chart-in-d--js)