# How do I create a flame graph using JavaScript and D3?
// plain

Creating a flame graph using JavaScript and D3 is a great way to visualize data. A flame graph is a type of chart that shows the relative amount of time spent on each function or process.

To create a flame graph, you will need to use the following code block:

```
const data = [
  {
    name: 'Function A',
    value: 10
  },
  {
    name: 'Function B',
    value: 5
  },
  {
    name: 'Function C',
    value: 15
  }
];

const svg = d3.select('svg');

const xScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.value)])
  .range([0, 500]);

const yScale = d3.scaleBand()
  .domain(data.map(d => d.name))
  .range([0, 200])
  .paddingInner(0.2);

const rects = svg.selectAll('rect')
  .data(data)
  .enter()
  .append('rect')
  .attr('width', d => xScale(d.value))
  .attr('height', yScale.bandwidth())
  .attr('x', 0)
  .attr('y', d => yScale(d.name))
  .attr('fill', '#f48024');
```

This code block will create a flame graph with three functions, A, B, and C. It will set the width of the rectangles to the value of the data points and the height to the band width of the yScale. The x and y attributes of the rectangles are set to 0 and the yScale of the data points respectively. The fill of the rectangles is also set to a color.

## Code explanation

- `const data`: This sets up an array of objects containing the data points for the graph.
- `const svg`: This sets up the SVG element that will be used to draw the graph.
- `const xScale`: This sets up a linear scale that will be used to set the width of the rectangles.
- `const yScale`: This sets up a band scale that will be used to set the height of the rectangles.
- `const rects`: This sets up the rectangles that will be drawn on the SVG element.

The output of the code will be a flame graph with three rectangles of different widths and heights.

## Helpful links
- [D3 Documentation](https://d3js.org/)
- [Flame Graph Tutorial](https://www.d3-graph-gallery.com/graph/heatmap_basic.html)

onelinerhub: [How do I create a flame graph using JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-flame-graph-using-javascript-and-d-)