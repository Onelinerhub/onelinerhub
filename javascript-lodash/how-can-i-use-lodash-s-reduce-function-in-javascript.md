# How can I use Lodash's reduce function in JavaScript?
// plain

The `reduce` function in Lodash is a powerful tool for transforming collections of data into a single value. It takes a collection, an accumulator function, and an optional initial value as its arguments. The accumulator function is called on each element of the collection, and the return value of the accumulator is passed as the accumulator for the next iteration. The optional initial value is used as the starting accumulator value for the first iteration.

For example, the following code block uses the `reduce` function to calculate the sum of an array of numbers:
```javascript
const numbers = [1,2,3,4,5];
const sum = _.reduce(numbers, (acc, num) => acc + num, 0);
console.log(sum); // Output: 15
```

The code works as follows:
- `numbers`: The array of numbers to be summed.
- `sum`: The variable that will store the result of the reduce operation.
- `_.reduce(numbers, (acc, num) => acc + num, 0)`: The reduce function, which takes the `numbers` array, an accumulator function that adds the current element to the accumulator, and an initial value of 0.
- `console.log(sum)`: Outputs the result of the reduce operation, which is 15.

Here are some useful links for further reading:
- [Lodash Documentation - reduce](https://lodash.com/docs/#reduce)
- [MDN - Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

onelinerhub: [How can I use Lodash's reduce function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-reduce-function-in-javascript)