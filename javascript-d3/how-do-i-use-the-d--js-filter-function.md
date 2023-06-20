# How do I use the d3.js filter function?
// plain

The `d3.js filter function` is used to filter an array of data. It takes a callback function as an argument, which is used to test each element of the array. If the callback function returns `true` for an element, then it is included in the new filtered array.

For example, the following code uses the `d3.js filter function` to filter an array of numbers and only return the numbers that are greater than 5:

```
let numbers = [1, 2, 5, 8, 10];

let filtered = numbers.filter(function(number){
  return number > 5;
});

console.log(filtered);
```

The output of the code would be:

```
[8, 10]
```

The code works by looping through each element in the array and passing it to the callback function. The callback function checks if the element is greater than 5, and if so, it is included in the new filtered array.

Parts of the code:
- `let numbers = [1, 2, 5, 8, 10];`: This creates an array of numbers.
- `let filtered = numbers.filter(function(number){`: This calls the `filter` function on the `numbers` array.
- `return number > 5;`: This is the callback function that is used to test each element in the array. It returns `true` if the element is greater than 5.

## Helpful links
- [d3.js filter function documentation](https://github.com/d3/d3-collection#filters)

onelinerhub: [How do I use the d3.js filter function?](https://onelinerhub.com/javascript-d3/how-do-i-use-the-d--js-filter-function)