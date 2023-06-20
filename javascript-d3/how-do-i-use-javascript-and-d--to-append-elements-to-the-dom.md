# How do I use JavaScript and D3 to append elements to the DOM?
// plain

To use JavaScript and D3 to append elements to the DOM, you can use the `.append()` method. This method takes a string argument that specifies the type of element you want to append, and then an optional second argument for the element's attributes.

For example, to append a `<p>` element to the DOM, you can use the following code:

```javascript
d3.select("body")
  .append("p")
  .attr("id", "new-paragraph")
  .text("This is a new paragraph!");
```

This will create the following output:

```
<p id="new-paragraph">This is a new paragraph!</p>
```

The code above consists of the following parts:

1. `d3.select("body")` - Selects the `<body>` element of the DOM
2. `.append("p")` - Appends a `<p>` element to the DOM
3. `.attr("id", "new-paragraph")` - Sets the `id` attribute of the `<p>` element to `new-paragraph`
4. `.text("This is a new paragraph!")` - Sets the text content of the `<p>` element to `This is a new paragraph!`

For more information, see the [D3 documentation on Appending Elements](https://github.com/d3/d3-selection#selection_append).

onelinerhub: [How do I use JavaScript and D3 to append elements to the DOM?](https://onelinerhub.com/javascript-d3/how-do-i-use-javascript-and-d--to-append-elements-to-the-dom)