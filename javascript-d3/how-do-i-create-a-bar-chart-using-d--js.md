# How do I create a bar chart using d3.js?
// plain

Creating a bar chart with D3.js is a simple process. To create a basic bar chart, you will need to include the D3 library in your HTML page, create a set of data, and then bind that data to the chart. Here is an example of code to create a basic bar chart:

```
<script src="https://d3js.org/d3.v5.min.js"></script>

<script>
  // Create Data
  const data = [
    {name: 'Apples', count: 10},
    {name: 'Oranges', count: 5},
    {name: 'Bananas', count: 20},
    {name: 'Pears', count: 8}
  ];

  // Create Chart
  const svg = d3.select('#chart')
    .append('svg')
    .attr('width', 400)
    .attr('height', 300);

  // Create Bars
  const bars = svg.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr('y', (d, i) => i * 25)
    .attr('width', d => d.count * 10)
    .attr('height', 20);

</script>
```

This code will create a basic bar chart with four bars, one for each item in the data set. The code can be broken down into the following parts:

1. Include D3 library in the HTML page.
2. Create a set of data to bind to the chart.
3. Select the element to which the chart will be appended.
4. Create a set of bars by binding the data to the chart.
5. Set the attributes of each bar (e.g. width, height, position).

For more information on creating bar charts with D3.js, see the [D3.js Documentation](https://github.com/d3/d3/wiki/Gallery) and [D3.js Tutorials](https://www.tutorialsteacher.com/d3js).

onelinerhub: [How do I create a bar chart using d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-create-a-bar-chart-using-d--js)