# How can I sort an array of objects by property using Lodash and JavaScript?
// plain

To sort an array of objects by property using Lodash and JavaScript, you can use the `_.sortBy` function. This function takes an array and a sorting function as arguments and returns a new array sorted according to the sorting function.

For example, to sort an array of objects by their `name` property, you can use the following code:

```
const arr = [
  {name: 'John', age: 25},
  {name: 'Alice', age: 22},
  {name: 'Bob', age: 28},
];

const sortedArr = _.sortBy(arr, 'name');

console.log(sortedArr);
// Output:
// [
//   {name: 'Alice', age: 22},
//   {name: 'Bob', age: 28},
//   {name: 'John', age: 25},
// ]
```

This code does the following:

1. Declares a `arr` array containing three objects.
2. Calls `_.sortBy` with `arr` and `name` as arguments.
3. Assigns the resulting array to `sortedArr`.
4. Logs `sortedArr` to the console.

## Helpful links

- [Lodash documentation - _.sortBy](https://lodash.com/docs/4.17.15#sortBy)
- [MDN JavaScript Reference - Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

onelinerhub: [How can I sort an array of objects by property using Lodash and JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-sort-an-array-of-objects-by-property-using-lodash-and-javascript)