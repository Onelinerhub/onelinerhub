# How do I use D3.js to create a Wikipedia page?
// plain

Using D3.js to create a Wikipedia page is relatively straightforward. The first step is to create a new HTML file and include the D3.js library.

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://d3js.org/d3.v4.min.js"></script>
</head>
<body>

</body>
</html>
```

The next step is to create a `<div>` element in the body of the HTML file. This `<div>` will be used as a container for the Wikipedia page content.

```html
<body>
  <div id="wikiPage"></div>
</body>
```

Then, use the `d3.select()` method to select the `<div>` and use the `.html()` method to set the HTML content of the `<div>` to the Wikipedia page content.

```javascript
d3.select("#wikiPage").html(`
  <h1>Wikipedia</h1>
  <p>Wikipedia is a free online encyclopedia, created and edited by volunteers around the world.</p>
`);
```

Finally, use the `d3.selectAll()` method to select all the elements in the `<div>` and use the `.style()` method to set styling for the elements.

```javascript
d3.selectAll("#wikiPage *").style("color", "blue");
```

The output of this code would be a Wikipedia page with all of the elements styled in blue.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [MDN Web Docs - Selecting Elements](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [MDN Web Docs - Setting Styles](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)

onelinerhub: [How do I use D3.js to create a Wikipedia page?](https://onelinerhub.com/javascript-d3/how-do-i-use-d--js-to-create-a-wikipedia-page)