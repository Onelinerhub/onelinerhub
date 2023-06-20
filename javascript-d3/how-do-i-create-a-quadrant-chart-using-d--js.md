# How do I create a quadrant chart using d3.js?
// plain

Creating a quadrant chart using d3.js requires a few steps.

1. First, create a `svg` element to hold the quadrant chart.
```
const svg = d3.select('body').append('svg')
  .attr('width', width)
  .attr('height', height);
```

2. Next, create an array of data points to plot on the quadrant chart.
```
const data = [
  {x: 10, y: 20, label: 'A'},
  {x: 20, y: 15, label: 'B'},
  {x: 30, y: 10, label: 'C'},
  {x: 40, y: 5, label: 'D'},
];
```

3. Create `x` and `y` scales to map data points to the chart.
```
const xScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.x)])
  .range([0, width]);

const yScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.y)])
  .range([height, 0]);
```

4. Draw the axes for the chart.
```
const xAxis = d3.axisBottom(xScale);
const yAxis = d3.axisLeft(yScale);

svg.append('g')
  .attr('transform', `translate(0, ${height})`)
  .call(xAxis);

svg.append('g')
  .call(yAxis);
```

5. Finally, draw the data points on the chart.
```
svg.selectAll('circle')
  .data(data)
  .enter()
  .append('circle')
  .attr('cx', d => xScale(d.x))
  .attr('cy', d => yScale(d.y))
  .attr('r', 5)
  .attr('fill', 'red');
```

The output should be a quadrant chart with four data points labeled A, B, C, and D.

## Helpful links
- [d3.js documentation](https://github.com/d3/d3/wiki)
- [Tutorial on creating a quadrant chart with d3.js](https://www.d3-graph-gallery.com/graph/scatter_quadrant.html)

onelinerhub: [How do I create a quadrant chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-quadrant-chart-using-d--js)