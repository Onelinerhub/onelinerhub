# How do I add a tooltip to a D3 graph using JavaScript?
// plain

To add a tooltip to a D3 graph using JavaScript, you must first create a div element with the id of 'tooltip'. This element will be used to display the tooltip when the user hovers over the graph.

Next, you must add an event listener to the graph that will detect when the user hovers over it. This can be done using the `on('mouseover', function(d))` method. Inside of the function, you must set the content of the tooltip div to the desired text.

```
d3.select("svg")
	.on('mouseover', function(d) {
		d3.select('#tooltip')
			.style('opacity', 1)
			.style('left', (d3.event.pageX) + 'px')
			.style('top', (d3.event.pageY) + 'px')
			.html('Tooltip text');
	});
```

Finally, you must also add an event listener for when the user moves the mouse away from the graph. This can be done using the `on('mouseout', function(d))` method. Inside of the function, you must set the opacity of the tooltip div to 0.

```
d3.select("svg")
	.on('mouseout', function(d) {
		d3.select('#tooltip')
			.style('opacity', 0);
	});
```

The resulting tooltip should look like this when the user hovers over the graph:

![alt text](https://i.stack.imgur.com/Q5pU6.png "Tooltip Example")

Parts of the code and their explanations:

- `d3.select("svg")`: Selects the SVG element that contains the graph.
- `.on('mouseover', function(d))`: Adds an event listener for when the user hovers over the graph.
- `d3.select('#tooltip')`: Selects the tooltip div element.
- `.style('opacity', 1)`: Sets the opacity of the tooltip to 1, making it visible.
- `.style('left', (d3.event.pageX) + 'px')`: Sets the left position of the tooltip to the x coordinate of the mouse.
- `.style('top', (d3.event.pageY) + 'px')`: Sets the top position of the tooltip to the y coordinate of the mouse.
- `.html('Tooltip text')`: Sets the content of the tooltip to the desired text.
- `.on('mouseout', function(d))`: Adds an event listener for when the user moves the mouse away from the graph.
- `.style('opacity', 0)`: Sets the opacity of the tooltip to 0, making it invisible.

## Helpful links
- [D3 Tooltip Tutorial](https://www.d3-graph-gallery.com/graph/interactivity_tooltip.html)
- [D3 Mouse Event Tutorial](https://www.d3-graph-gallery.com/graph/interactivity_mouseover.html)

onelinerhub: [How do I add a tooltip to a D3 graph using JavaScript?](https://onelinerhub.com/javascript-d3/how-do-i-add-a-tooltip-to-a-d--graph-using-javascript)