# How do I set up the x axis in d3.js?
// plain

Setting up the x axis in d3.js is done with the `scaleLinear()` function, which takes a domain and range. The domain is the range of values that the axis will represent, while the range is the pixel range that the axis will be displayed on.

For example, the following code will create an x axis that goes from 0 to 10, with a range of 0 to 500 pixels:

```javascript
var x = d3.scaleLinear()
    .domain([0, 10])
    .range([0, 500]);
```

## Code explanation


- `scaleLinear()`: the function used to create the x axis.
- `domain`: the range of values the axis will represent.
- `range`: the pixel range that the axis will be displayed on.

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [ScaleLinear](https://github.com/d3/d3-scale/blob/master/README.md#scaleLinear)

onelinerhub: [How do I set up the x axis in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-set-up-the-x-axis-in-d--js)