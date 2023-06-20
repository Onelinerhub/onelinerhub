# How can I use D3.js Observable to create interactive data visualizations?
// plain

Creating interactive data visualizations with D3.js Observable is easy and straightforward.

Here is an example of how to create a basic scatter plot with a tooltip using D3.js Observable:

```
import {scatter, select} from "@d3/mitch-dataviz";

const data = [
  {x: 10, y: 20},
  {x: 15, y: 25},
  {x: 20, y: 30}
];

const width = 500;
const height = 500;

scatter()
  .width(width)
  .height(height)
  .data(data)
  .render();

select("circle")
  .on("mouseover", d => console.log(d))
  .on("mouseout", () => console.log("mouseout"));
```

When a user hovers over a circle, the data object associated with the circle will be logged to the console.

The code above consists of the following parts:

1. Importing the `scatter` and `select` functions from the `@d3/mitch-dataviz` library
2. Defining the data to be used for the visualization
3. Setting the width and height of the visualization
4. Calling the `scatter` function to render the visualization
5. Using the `select` function to select the circles in the visualization and attaching `mouseover` and `mouseout` event handlers that log data to the console

For more information, see the [D3.js Observable documentation](https://observablehq.com/@d3/introduction).

onelinerhub: [How can I use D3.js Observable to create interactive data visualizations?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--js-observable-to-create-interactive-data-visualizations)