# How can I use Lodash to filter an array in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to filter an array in JavaScript by using the `_.filter()` function.

The `_.filter()` function takes two arguments: an array and a predicate function. The predicate function is a function that returns `true` or `false` for each element in the array.

## Example


```
const array = [1, 2, 3, 4, 5];

const result = _.filter(array, (element) => element % 2 === 0);

console.log(result);
// Output: [2, 4]
```

In the example above, the predicate function `(element) => element % 2 === 0` checks if the element is even or odd. If the element is even, it returns `true` and the element is added to the result array.

The `_.filter()` function can also be used with an object array. The predicate function should return `true` or `false` based on the object property values.

## Example


```
const array = [
  { name: 'John', age: 25 },
  { name: 'Jane', age: 18 },
  { name: 'Joe', age: 32 },
];

const result = _.filter(array, (element) => element.age >= 21);

console.log(result);
// Output: [{ name: 'John', age: 25 }, { name: 'Joe', age: 32 }]
```

In the example above, the predicate function `(element) => element.age >= 21` checks if the age of the element is greater than or equal to 21. If the condition is true, it returns `true` and the element is added to the result array.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN Array Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

onelinerhub: [How can I use Lodash to filter an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-filter-an-array-in-javascript)