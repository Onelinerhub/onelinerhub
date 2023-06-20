# How to create a Gantt chart using D3.js?
// plain

Creating a Gantt chart using D3.js is a great way to visualize project timelines and progress. The following example code uses D3.js to create a Gantt chart:

```
// Create SVG
var svg = d3.select("body")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

// Create scales
var xScale = d3.scaleTime()
               .domain([d3.min(data, d => d.startTime), d3.max(data, d => d.endTime)])
               .range([0, width]);

var yScale = d3.scaleBand()
               .domain(data.map(d => d.name))
               .range([0, height]);

// Create Gantt chart
svg.selectAll("rect")
   .data(data)
   .enter()
   .append("rect")
   .attr("x", d => xScale(d.startTime))
   .attr("y", d => yScale(d.name))
   .attr("width", d => xScale(d.endTime) - xScale(d.startTime))
   .attr("height", yScale.bandwidth());
```

This code will create an SVG element, create two scales (xScale and yScale) to map data values to the chart's x and y axes, and then create a Gantt chart by appending rectangles to the SVG element. The rectangles are positioned using the x and y scales, and their width and height are based on the data's start and end times.

The code consists of the following parts:

1. Creation of SVG element: `var svg = d3.select("body").append("svg").attr("width", width).attr("height", height);`
2. Creation of xScale: `var xScale = d3.scaleTime().domain([d3.min(data, d => d.startTime), d3.max(data, d => d.endTime)]).range([0, width]);`
3. Creation of yScale: `var yScale = d3.scaleBand().domain(data.map(d => d.name)).range([0, height]);`
4. Creation of Gantt chart: `svg.selectAll("rect").data(data).enter().append("rect").attr("x", d => xScale(d.startTime)).attr("y", d => yScale(d.name)).attr("width", d => xScale(d.endTime) - xScale(d.startTime)).attr("height", yScale.bandwidth());`

For more information on creating Gantt charts using D3.js, please see the following links:

- [Creating a Basic Gantt Chart with D3.js](https://medium.com/@nick.hartley/creating-a-basic-gantt-chart-with-d3-js-d3fc-8e2d1c8c1d09)
- [D3 Gantt Chart Tutorial](https://blog.risingstack.com/d3-js-tutorial-bar-charts-with-javascript/)

onelinerhub: [How to create a Gantt chart using D3.js?](https://onelinerhub.com/javascript-d3/how-to-create-a-gantt-chart-using-d--js)