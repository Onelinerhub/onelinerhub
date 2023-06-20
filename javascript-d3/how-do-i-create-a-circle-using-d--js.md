# How do I create a circle using D3.js?
// plain

Creating a circle using D3.js is a relatively simple process. To do this, the following code can be used:

```
var svg = d3.select('body').append('svg');

var circle = svg.append('circle')
    .attr('cx', 50)
    .attr('cy', 50)
    .attr('r', 20)
    .style('fill', 'red');
```

This code will create a circle with a radius of 20, centered at the coordinates (50, 50), and filled with the color red.

The code can be broken down into a few parts:

1. Select the body and append an svg element: `var svg = d3.select('body').append('svg');`
2. Append a circle to the svg element: `var circle = svg.append('circle');`
3. Set the coordinates of the circle: `.attr('cx', 50) .attr('cy', 50);`
4. Set the radius of the circle: `.attr('r', 20);`
5. Set the fill color of the circle: `.style('fill', 'red');`

For more information, please refer to the following links:
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Tutorials](https://www.d3indepth.com/tutorials/)

onelinerhub: [How do I create a circle using D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-circle-using-d--js)