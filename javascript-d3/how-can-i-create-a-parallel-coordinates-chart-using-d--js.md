# How can I create a parallel coordinates chart using d3.js?
// plain

Creating a parallel coordinates chart using d3.js is easy and straightforward.

First, you need to create a basic HTML page with a `<div>` element to hold the chart.

```
<!DOCTYPE html>
<html>
  <head>
    <title>Parallel Coordinates Chart</title>
  </head>
  <body>
    <div id="chart"></div>
  </body>
</html>
```

Then, you need to include the d3.js library in the `<head>` section of your HTML page.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

Next, define the dataset you want to use for the chart.

```
var dataset = [
  {name: "John", age: 20, height: 170},
  {name: "Jane", age: 25, height: 160},
  {name: "Joe", age: 30, height: 180}
];
```

Create a `<svg>` element to hold the chart.

```
var svg = d3.select("#chart")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);
```

Define the scales for the axes.

```
var xScale = d3.scaleLinear()
               .domain([0, d3.max(dataset, function(d) { return d.age; })])
               .range([0, width]);

var yScale = d3.scaleLinear()
               .domain([0, d3.max(dataset, function(d) { return d.height; })])
               .range([height, 0]);
```

Create the axes.

```
var xAxis = d3.axisBottom(xScale);

var yAxis = d3.axisLeft(yScale);

svg.append("g")
   .attr("class", "x axis")
   .attr("transform", "translate(0," + height + ")")
   .call(xAxis);

svg.append("g")
   .attr("class", "y axis")
   .call(yAxis);
```

Finally, create the lines for the chart.

```
svg.selectAll("line")
   .data(dataset)
   .enter()
   .append("line")
   .attr("x1", function(d) { return xScale(d.age); })
   .attr("y1", function(d) { return yScale(d.height); })
   .attr("x2", function(d) { return xScale(d.age); })
   .attr("y2", height)
   .attr("stroke", "gray")
   .attr("stroke-width", "1px");
```

This is all that is needed to create a basic parallel coordinates chart using d3.js.

## Code explanation
**

1. Include d3.js library in the `<head>` section of HTML page:
```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

2. Define the dataset:
```
var dataset = [
  {name: "John", age: 20, height: 170},
  {name: "Jane", age: 25, height: 160},
  {name: "Joe", age: 30, height: 180}
];
```

3. Create a `<svg>` element to hold the chart:
```
var svg = d3.select("#chart")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);
```

4. Define the scales for the axes:
```
var xScale = d3.scaleLinear()
               .domain([0, d3.max(dataset, function(d) { return d.age; })])
               .range([0, width]);

var yScale = d3.scaleLinear()
               .domain([0, d3.max(dataset, function(d) { return d.height; })])
               .range([height, 0]);
```

5. Create the axes:
```
var xAxis = d3.axisBottom(xScale);

var yAxis = d3.axisLeft(yScale);

svg.append("g")
   .attr("class", "x axis")
   .attr("transform", "translate(0," + height + ")")
   .call(xAxis);

svg.append("g")
   .attr("class", "y axis")
   .call(yAxis);
```

6. Create the lines for the chart:
```
svg.selectAll("line")
   .data(dataset)
   .enter()
   .append("line")
   .attr("x1", function(d) { return xScale(d.age); })
   .attr("y1", function(d) { return yScale(d.height); })
   .attr("x2", function(d) { return xScale(d.age); })
   .attr("y2", height)
   .attr("stroke", "gray")
   .attr("stroke-width", "1px");
```

**## Helpful links**

- https://d3js.org/
- https://observablehq.com/@d3/parallel-coordinates

onelinerhub: [How can I create a parallel coordinates chart using d3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-parallel-coordinates-chart-using-d--js)