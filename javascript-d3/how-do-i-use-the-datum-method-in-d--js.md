# How do I use the datum method in D3.js?
// plain

The datum method in D3.js is used to set or retrieve the data associated with an element. It is often used within the enter() selection to bind data to elements.

## Example

```
var selection = d3.selectAll("div")
    .data([1,2,3])
    .enter()
    .append("div")
    .datum(function(d) { // set the data
        return d * 10;
    });

console.log(selection.datum()); // retrieve the data
```
## Output example

`[10, 20, 30]`

In the example above, the datum() method was used to set the data associated with the div elements to an array of numbers multiplied by 10. The datum() method was also used to retrieve the data associated with the div elements, which is printed to the console.

## Code explanation

1. `d3.selectAll("div")`: This line selects all div elements on the page.
2. `.data([1,2,3])`: This line binds the data array [1,2,3] to the selected div elements.
3. `.enter()`: This line creates a placeholder for each data element in the array.
4. `.append("div")`: This line appends a div element for each placeholder.
5. `.datum(function(d) { // set the data`: This line sets the data associated with each div element to the value returned by the callback function.
6. `return d * 10;`: This line returns the value of each data element multiplied by 10.
7. `selection.datum()`: This line retrieves the data associated with the div elements.

## Helpful links
- [D3.js Documentation](https://github.com/d3/d3/blob/master/API.md#selections-d3_selection)
- [Datum Method Tutorial](https://www.d3-graph-gallery.com/graph/custom_legend.html)

onelinerhub: [How do I use the datum method in D3.js?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-datum-method-in-d--js)