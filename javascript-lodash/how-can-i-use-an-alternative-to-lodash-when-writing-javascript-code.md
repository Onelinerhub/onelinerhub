# How can I use an alternative to Lodash when writing JavaScript code?
// plain

An alternative to Lodash when writing JavaScript code is to use the native JavaScript language itself. JavaScript has many built-in methods that can be used to achieve the same goals as Lodash.

For example, the `Array.prototype.map()` method can be used to iterate over an array and create a new array with the results of calling a provided function on every element in the array:

```
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(number => number * 2);

console.log(doubled);
// Output: [2, 4, 6, 8, 10]
```

The `Array.prototype.map()` method takes a callback function as its first argument, which is invoked with three arguments:

1. The current element being processed in the array
2. The index of the current element being processed in the array
3. The array that `map()` was called upon

The `map()` method then returns a new array with the results of calling the callback function for each element in the array.

Other native JavaScript methods that can be used to replace Lodash include `Array.prototype.filter()`, `Array.prototype.reduce()`, `Array.prototype.find()`, `Array.prototype.some()`, and `Array.prototype.every()`.

## Helpful links

- [MDN Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
- [MDN Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [MDN Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
- [MDN Array.prototype.find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
- [MDN Array.prototype.some()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
- [MDN Array.prototype.every()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)

onelinerhub: [How can I use an alternative to Lodash when writing JavaScript code?](https://onelinerhub.com/javascript-lodash/how-can-i-use-an-alternative-to-lodash-when-writing-javascript-code)