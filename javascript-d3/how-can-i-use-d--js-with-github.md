# How can I use d3.js with Github?
// plain

To use d3.js with Github, you first need to create a repository on Github and clone it to your local machine. Then, create an index.html file in the repository and add the following code to it:

```
<!DOCTYPE html>
<html>
  <head>
    <title>d3.js with Github</title>
  </head>
  <body>
    <script src="https://d3js.org/d3.v5.min.js"></script>
    <script>
      // Your d3.js code here
    </script>
  </body>
</html>
```

Next, you need to add the d3.js library to your code. This can be done by adding a `<script>` tag to the `<head>` of the index.html file, like this:

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Now, you can add your d3.js code in the `<script>` tag. For example, you can add the following code to draw a circle in the SVG:

```
<script>
  var svg = d3.select("body")
    .append("svg")
    .attr("width", 500)
    .attr("height", 500);

  svg.append("circle")
    .attr("cx", 250)
    .attr("cy", 250)
    .attr("r", 30)
    .style("fill", "red");
</script>
```

This will draw a red circle with radius of 30px at the center of the SVG.

After that, you can commit the changes to the Github repository and push them to the remote repository.

**Parts of the code and explanation:**
- `<script src="https://d3js.org/d3.v5.min.js"></script>`: This adds the d3.js library to the page.
- `var svg = d3.select("body")`: This selects the body element of the page.
- `.append("svg")`: This appends an SVG element to the body element.
- `.attr("width", 500)` and `.attr("height", 500)`: This sets the width and height of the SVG element.
- `svg.append("circle")`: This adds a circle element to the SVG.
- `.attr("cx", 250)`, `.attr("cy", 250)`, and `.attr("r", 30)`: This sets the x and y coordinates and radius of the circle.
- `.style("fill", "red")`: This sets the fill color of the circle to red.

**## Helpful links**
- [d3.js documentation](https://github.com/d3/d3/blob/master/API.md)
- [Github documentation](https://help.github.com/en)

onelinerhub: [How can I use d3.js with Github?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--js-with-github)