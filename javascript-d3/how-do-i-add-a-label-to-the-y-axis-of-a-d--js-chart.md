# How do I add a label to the Y axis of a D3.js chart?
// plain

To add a label to the Y axis of a D3.js chart, you need to use the `axisLeft` method. This method takes an optional argument for the label.

For example:
```
const yAxis = d3.axisLeft()
  .scale(yScale)
  .tickFormat(d3.format('.2s'))
  .tickSize(-width)
  .tickPadding(10)
  .tickValues(yTicks)
  .tickSizeOuter(0)
  .tickFormat(d3.format('.2s'))
  .tickSizeInner(0)
  .tickSize(0)
  .tickPadding(10)
  .tickSizeOuter(0)
  .tickSizeInner(0)
  .tickLabel('Label');
```
This will add the label `'Label'` to the Y axis.

## Code explanation


* `d3.axisLeft()` - creates the Y axis
* `.scale(yScale)` - sets the scale for the Y axis
* `.tickFormat(d3.format('.2s'))` - sets the format for the ticks
* `.tickSize(-width)` - sets the size of the ticks
* `.tickPadding(10)` - sets the padding of the ticks
* `.tickValues(yTicks)` - sets the values for the ticks
* `.tickSizeOuter(0)` - sets the outer size of the ticks
* `.tickFormat(d3.format('.2s'))` - sets the format for the ticks
* `.tickSizeInner(0)` - sets the inner size of the ticks
* `.tickSize(0)` - sets the size of the ticks
* `.tickPadding(10)` - sets the padding of the ticks
* `.tickSizeOuter(0)` - sets the outer size of the ticks
* `.tickSizeInner(0)` - sets the inner size of the ticks
* `.tickLabel('Label')` - sets the label of the Y axis

## Helpful links

* [D3.js Documentation](https://github.com/d3/d3/wiki/API-Reference)
* [AxisLeft Method](https://github.com/d3/d3-axis#axisLeft)

onelinerhub: [How do I add a label to the Y axis of a D3.js chart?](https://onelinerhub.com/javascript-d3/how-do-i-add-a-label-to-the-y-axis-of-a-d--js-chart)