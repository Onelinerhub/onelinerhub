# How do I use Lodash to sort an array of objects by a specific key in JavaScript?
// plain

Using Lodash to sort an array of objects by a specific key in JavaScript is a simple task.

```
var _ = require('lodash');

var array = [
  { name: 'John', age: 30 },
  { name: 'Jane', age: 25 },
  { name: 'Mike', age: 35 },
];

var sortedArray = _.sortBy(array, 'age');

console.log(sortedArray);
```

## Output example

```
[
  { name: 'Jane', age: 25 },
  { name: 'John', age: 30 },
  { name: 'Mike', age: 35 }
]
```

The code above uses the Lodash `sortBy` method to sort an array of objects by the `age` key. The `sortBy` method takes two arguments: the array to be sorted and the key by which the array should be sorted. The array is then sorted in ascending order according to the value of the specified key.

## Code explanation


1. `var _ = require('lodash');` - imports the Lodash library
2. `var array = [ ... ]` - array of objects to be sorted
3. `var sortedArray = _.sortBy(array, 'age');` - uses the Lodash `sortBy` method to sort the array according to the `age` key
4. `console.log(sortedArray);` - prints the sorted array to the console

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [MDN Documentation on Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

onelinerhub: [How do I use Lodash to sort an array of objects by a specific key in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-sort-an-array-of-objects-by-a-specific-key-in-javascript)