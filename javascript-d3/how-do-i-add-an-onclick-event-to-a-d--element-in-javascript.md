# How do I add an onclick event to a D3 element in Javascript?
// plain

Adding an onclick event to a D3 element in Javascript is relatively simple. The following example code block demonstrates how to do this:

```
d3.select("body")
  .append("div")
  .attr("id", "myDiv")
  .on("click", function(){
    alert("You clicked the div!");
  });
```

When the div is clicked, the alert "You clicked the div!" will appear. The code above does the following:

1. `d3.select("body")` - selects the body element
2. `.append("div")` - appends a div element to the body
3. `.attr("id", "myDiv")` - assigns the div an id of "myDiv"
4. `.on("click", function(){...})` - adds a click event listener to the div

When the div is clicked, the anonymous function passed to the `.on()` method will be called.

For more information on adding events to D3 elements, see the [D3 documentation](https://github.com/d3/d3/blob/master/API.md#selection_on).

onelinerhub: [How do I add an onclick event to a D3 element in Javascript?](https://onelinerhub.com/javascript-d3/how-do-i-add-an-onclick-event-to-a-d--element-in-javascript)