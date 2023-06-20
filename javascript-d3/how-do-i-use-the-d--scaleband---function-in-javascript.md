# How do I use the d3 scaleBand() function in JavaScript?
// plain

The `d3.scaleBand()` function is used to create a quantitative scale with discrete output values. It takes an array of values as input and outputs a value for each element in the array. This is useful for creating a discrete scale, such as for bar charts and histograms.

```javascript
// example code
var data = [1, 2, 3, 4, 5];

var x = d3.scaleBand()
  .domain(data)
  .range([0, 100]);

console.log(x(2)); // 20
```

The output of the example code is `20`.

The code consists of three parts:

1. A `data` array which contains the input values.
2. A `d3.scaleBand()` function which creates a new scale. It takes two arguments: `domain` which is the array of input values, and `range` which is an array of output values.
3. A `x(2)` function which takes the input value 2 from the `data` array and returns the corresponding output value from the `range` array, in this case `20`.

## Helpful links

- [d3-scale](https://github.com/d3/d3-scale)
- [d3-scale-band](https://github.com/d3/d3-scale#scaleBand)

onelinerhub: [How do I use the d3 scaleBand() function in JavaScript?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-d--scaleband---function-in-javascript)