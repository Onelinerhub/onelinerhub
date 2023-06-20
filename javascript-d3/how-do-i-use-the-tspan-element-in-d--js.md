# How do I use the tspan element in D3.js?
// plain

The `tspan` element in D3.js is used to break text into multiple lines or to set the position of a text element. It can be used to control the styling of the text by setting the font size, font family, font weight, and other properties.

For example, to set the font size to `12px` and font family to `Arial` for a `text` element:

```
d3.select("text")
    .attr("fill", "black")
    .selectAll("tspan")
    .data(["Hello", "World"])
    .enter()
    .append("tspan")
    .attr("x", 0)
    .attr("y", function(d, i) { return i * 20; })
    .attr("font-size", "12px")
    .attr("font-family", "Arial")
    .text(function(d) { return d; });
```

The output of the above code is two lines of text with font size of `12px` and font family of `Arial`:

```
Hello
World
```

## Code explanation


- `d3.select("text")`: Selects the `text` element from the DOM.
- `.attr("fill", "black")`: Sets the fill color of the `text` element to `black`.
- `.selectAll("tspan")`: Selects all `tspan` elements within the `text` element.
- `.data(["Hello", "World"])`: Binds the data array to the `tspan` elements.
- `.enter()`: Creates new `tspan` elements for each data item.
- `.append("tspan")`: Appends the `tspan` elements to the DOM.
- `.attr("x", 0)`: Sets the x-coordinate of the `tspan` elements to `0`.
- `.attr("y", function(d, i) { return i * 20; })`: Sets the y-coordinate of the `tspan` elements to `0`, `20`, `40`, etc.
- `.attr("font-size", "12px")`: Sets the font size of the `tspan` elements to `12px`.
- `.attr("font-family", "Arial")`: Sets the font family of the `tspan` elements to `Arial`.
- `.text(function(d) { return d; })`: Sets the text content of the `tspan` elements to the corresponding data item.

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/blob/master/API.md#selecting-elements)
- [MDN - SVG tspan element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan)

onelinerhub: [How do I use the tspan element in D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-tspan-element-in-d--js)