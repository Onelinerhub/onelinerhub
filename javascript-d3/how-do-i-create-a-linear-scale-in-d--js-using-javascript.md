# How do I create a linear scale in D3.js using JavaScript?
// plain

Creating a linear scale in D3.js using JavaScript is a fairly straightforward process. To begin, you'll need to include the D3 library in your HTML file.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Once the library is included, you can create the linear scale by specifying the domain and range:

```
var x = d3.scaleLinear()
    .domain([0, 100])
    .range([0, 600]);
```

In the example above, the domain is set to the range of 0-100, and the range is set to 0-600. The output of the scale is a function that can be used to map values from the domain to the range. For example, if we pass the value 50 to the scale, it will return 300:

```
x(50); // returns 300
```

## Code explanation


* `d3.scaleLinear()` - creates a linear scale
* `.domain([0, 100])` - sets the input domain
* `.range([0, 600])` - sets the output range
* `x(50)` - passes a value to the scale, returns the output

## Helpful links

* [D3.js Documentation](https://github.com/d3/d3/blob/master/API.md#scales-d3-scale)
* [MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/scaleLinear)

onelinerhub: [How do I create a linear scale in D3.js using JavaScript?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-linear-scale-in-d--js-using-javascript)