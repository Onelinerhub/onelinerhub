# How can I create a word cloud using d3.js?
// plain

Creating a word cloud using d3.js is a relatively simple process. The code below demonstrates how to create a basic word cloud using d3.js.

```
<!DOCTYPE html>
<html>
<head>
  <title>Word Cloud Example</title>
  <script src="https://d3js.org/d3.v4.min.js"></script>
</head>
<body>
  <div id="wordCloud"></div>
  <script>
    // Create the data array
    var data = [
      {text: "d3.js", size: 30},
      {text: "Word Cloud", size: 20},
      {text: "Example", size: 10}
    ];

    // Create the SVG
    var svg = d3.select("#wordCloud").append("svg")
      .attr("width", 500)
      .attr("height", 500);

    // Create the layout
    var layout = d3.layout.cloud()
      .size([500, 500])
      .words(data)
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw);

    // Draw the words
    layout.start();
    function draw(words) {
      svg.append("g")
        .attr("transform", "translate(250,250)")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", "#000000")
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
    }
  </script>
</body>
</html>
```

This code will produce a word cloud with three words - "d3.js", "Word Cloud", and "Example" - with different font sizes based on the size specified in the data array.

The code consists of the following parts:

1. Create the data array: This is where you specify the words and their font sizes.
2. Create the SVG: This creates the SVG element which will contain the word cloud.
3. Create the layout: This sets up the parameters for the word cloud, including the font, font size, padding, and rotation.
4. Draw the words: This uses the data and layout parameters to draw the words onto the SVG.

For more information, see the [d3.js documentation](https://github.com/d3/d3/wiki) and the [word cloud example](https://bl.ocks.org/mbostock/4063269).

onelinerhub: [How can I create a word cloud using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-word-cloud-using-d--js)