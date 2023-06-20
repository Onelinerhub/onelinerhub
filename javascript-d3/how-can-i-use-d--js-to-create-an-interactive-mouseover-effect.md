# How can I use d3.js to create an interactive mouseover effect?
// plain

Using d3.js, you can create an interactive mouseover effect by binding data to elements and using the `on()` method to add event listeners. For example, the following code will create an SVG circle and change its radius on mouseover:

```javascript
d3.select('svg')
  .append('circle')
  .attr('cx', 50)
  .attr('cy', 50)
  .attr('r', 10)
  .on('mouseover', function() {
    d3.select(this).attr('r', 20);
  });
```

## Code explanation


1. `d3.select('svg')` - This selects the SVG element to which the circle will be appended.
2. `.append('circle')` - This appends a circle element to the SVG element.
3. `.attr('cx', 50)` - This sets the x-coordinate of the circle's center to 50.
4. `.attr('cy', 50)` - This sets the y-coordinate of the circle's center to 50.
5. `.attr('r', 10)` - This sets the radius of the circle to 10.
6. `.on('mouseover', function() { ... })` - This adds an event listener for the mouseover event.
7. `d3.select(this).attr('r', 20);` - This sets the radius of the circle to 20 when the mouseover event is triggered.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [D3.js Tutorials](https://www.dashingd3js.com/d3js-tutorials)

onelinerhub: [How can I use d3.js to create an interactive mouseover effect?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--js-to-create-an-interactive-mouseover-effect)