# How do I create a D3.js gallery?
// plain

Creating a D3.js gallery is a great way to showcase your data visualizations. Here's a quick guide on how to do it:

1. Start by gathering your data visualizations in a folder.

2. Create a `index.html` file in the same folder and add the following code:
```html
<html>
  <head>
    <title>My D3.js Gallery</title>
  </head>
  <body>
  </body>
</html>
```
3. Add the D3.js library to the `<head>` of the `index.html` file:
```html
<script src="https://d3js.org/d3.v4.min.js"></script>
```
4. Create a `<div>` element in the `<body>` of the `index.html` file:
```html
<div id="gallery"></div>
```
5. Add JavaScript code to the `<script>` tag of the `index.html` file to loop through the data visualizations and append them to the `<div>` element:
```javascript
var gallery = d3.select("#gallery");

d3.json("data.json", function(data) {
  data.forEach(function(d) {
    var div = gallery.append("div")
      .attr("class", "chart");

    div.append("img")
      .attr("src", d.image);

    div.append("p")
      .text(d.title);
  });
});
```
6. Finally, add some basic styling to the `index.html` file to make the gallery look nice:
```css
#gallery {
  display: flex;
  flex-wrap: wrap;
}

.chart {
  width: 300px;
  margin: 10px;
}
```
7. Open the `index.html` file in a web browser to see the gallery!

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [Getting Started with D3.js](https://d3js.org/#getting-started)

onelinerhub: [How do I create a D3.js gallery?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-d--js-gallery)