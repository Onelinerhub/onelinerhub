# How do I update data in d3.js?
// plain

Updating data in d3.js can be done with the `.data()` function. This function takes an array of data and joins it with the elements in the selection. The data is then passed through the enter, update, and exit selections, allowing you to add, modify, and remove elements accordingly.

For example, the following code block takes an array of data, binds it to the elements in the selection, and then uses the enter, update, and exit selections to update the elements accordingly.

```
var data = [4, 8, 15, 16, 23, 42];

d3.select("body").selectAll("p")
  .data(data)
  .enter().append("p")
  .text(function(d) { return "I’m number " + d + "!"; })
  .style("color", function(d) {
    if (d > 15) { return "red"; }
    else { return "black"; }
  });
```

This code will output six `<p>` tags with text saying "I'm number x!", where x is the respective number in the data array. The color of the text will be red if the number is greater than 15, and black otherwise.

The code can be broken down into the following parts:

1. `var data = [4, 8, 15, 16, 23, 42];` - this declares an array of data to be used in the update.
2. `d3.select("body").selectAll("p")` - this selects all `<p>` tags in the `<body>` element.
3. `.data(data)` - this binds the data array to the selection.
4. `.enter().append("p")` - this appends a new `<p>` tag for each element in the data array.
5. `.text(function(d) { return "I’m number " + d + "!"; })` - this sets the text of each `<p>` tag to "I'm number x!", where x is the respective number in the data array.
6. `.style("color", function(d) { if (d > 15) { return "red"; } else { return "black"; } });` - this sets the color of the text to red if the number is greater than 15, and black otherwise.

For more information, you can check out the [d3 documentation](https://github.com/d3/d3/wiki) or this [tutorial](https://www.d3indepth.com/enterexit/).

onelinerhub: [How do I update data in d3.js?](https://onelinerhub.com/javascript-d3/how-do-i-update-data-in-d--js)