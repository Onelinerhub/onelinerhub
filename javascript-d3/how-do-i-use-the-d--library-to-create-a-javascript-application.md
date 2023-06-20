# How do I use the D3 library to create a JavaScript application?
// plain

The D3 library is a powerful JavaScript library for creating interactive data visualizations in web browsers. To use the library, you must include the D3 library in your HTML page:

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Next, you can use the library to create a JavaScript application. For example, the code below creates a bar chart using D3:

```
var dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

var svgWidth = 500, svgHeight = 300, barPadding = 5;
var barWidth = (svgWidth / dataset.length);

var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var barChart = svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("y", function(d) {
         return svgHeight - d
    })
    .attr("height", function(d) {
        return d;
    })
    .attr("width", barWidth - barPadding)
    .attr("transform", function (d, i) {
        var translate = [barWidth * i, 0];
        return "translate("+ translate +")";
    });
```

The code above does the following:

1. Declares a dataset array of numbers
2. Creates a SVG element with a width and height
3. Selects all rect elements and binds the dataset to them
4. Appends a rect element for each item in the dataset
5. Sets the y-axis position, height, width, and transformation of each bar

The output of this code is a bar chart:

![Bar Chart](https://miro.medium.com/max/1400/1*KfqS-N-3dA-jm3_yLX2fQw.png)

For more information about using the D3 library, check out the [D3 documentation](https://github.com/d3/d3/wiki).

onelinerhub: [How do I use the D3 library to create a JavaScript application?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-d--library-to-create-a-javascript-application)