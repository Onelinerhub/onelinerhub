# How do I use JavaScript and D3 to create an SVG?
// plain

Using JavaScript and D3, we can create an SVG (Scalable Vector Graphic) with the following steps:

1. Create a `<svg>` element in the DOM:
```javascript
var svg = d3.select("body")
  .append("svg")
  .attr("width", 500)
  .attr("height", 300);
```
This code creates a `<svg>` element and appends it to the body of the HTML page. We set the width and height of the SVG to 500 and 300 respectively.

2. Create shapes inside the `<svg>` element:
```javascript
var rect = svg.append("rect")
  .attr("x", 10)
  .attr("y", 10)
  .attr("width", 100)
  .attr("height", 50)
  .attr("fill", "blue");
```
The code above creates a rectangle inside the `<svg>` element and sets its attributes such as x and y coordinates, width and height, and fill color.

3. Create text inside the `<svg>` element:
```javascript
var text = svg.append("text")
  .attr("x", 20)
  .attr("y", 50)
  .attr("fill", "red")
  .text("Hello World!");
```
The code above creates a text element inside the `<svg>` element and sets its attributes such as x and y coordinates and fill color. The text content is set to "Hello World!".

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [MDN SVG Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial)

onelinerhub: [How do I use JavaScript and D3 to create an SVG?](https://onelinerhub.com/javascript-d3/how-do-i-use-javascript-and-d--to-create-an-svg)