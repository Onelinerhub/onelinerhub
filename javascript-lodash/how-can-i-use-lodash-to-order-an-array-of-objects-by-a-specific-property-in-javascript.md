# How can I use Lodash to order an array of objects by a specific property in JavaScript?
// plain

Using Lodash, you can easily order an array of objects by a specific property in JavaScript. The following example code demonstrates how to do this:

```
// array of objects
const arr = [
  {name: 'John', age: 20},
  {name: 'Tom', age: 18},
  {name: 'Bob', age: 19}
];

// order array of objects by the age property
const orderedArr = _.orderBy(arr, ['age'], ['asc']);

console.log(orderedArr);
```

## Output example

```
[
  {name: 'Tom', age: 18},
  {name: 'Bob', age: 19},
  {name: 'John', age: 20}
]
```

## Code explanation

1. `const arr`: creates a constant variable `arr` which stores an array of objects.
2. `_.orderBy()`: uses Lodash's `orderBy` function to order the `arr` array of objects by the `age` property in ascending order.
3. `console.log()`: prints the ordered array of objects to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [MDN Documentation on `_.orderBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

onelinerhub: [How can I use Lodash to order an array of objects by a specific property in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-order-an-array-of-objects-by-a-specific-property-in-javascript)