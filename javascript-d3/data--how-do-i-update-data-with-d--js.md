# data

How do I update data with d3.js?
// plain

Updating data with d3.js is a relatively simple process. To update data, you need to use the `d3.select()` and `.data()` methods. The `d3.select()` method selects the elements that you want to update, and the `.data()` method binds the data to the elements.

For example, if you had a set of divs with the class `.bar`, and you wanted to update the data bound to them, you could use the following code:

```javascript
d3.selectAll('.bar')
  .data([20, 30, 40, 50])
  .style('width', d => `${d}px`);
```

This code would update the data bound to the `.bar` elements to `[20, 30, 40, 50]`, and set the width of each div to the corresponding value in the data array.

The code consists of the following parts:

- `d3.selectAll('.bar')`: Selects all elements with the class `.bar`.
- `.data([20, 30, 40, 50])`: Binds the data `[20, 30, 40, 50]` to the elements.
- `.style('width', d => `${d}px`)`: Sets the width of each element to the corresponding data value, plus the string `"px"`.

For more information on updating data with d3.js, see the [d3.js documentation](https://github.com/d3/d3/blob/master/API.md#data).

onelinerhub: [data

How do I update data with d3.js?](https://onelinerhub.com/javascript-d3/data--how-do-i-update-data-with-d--js)