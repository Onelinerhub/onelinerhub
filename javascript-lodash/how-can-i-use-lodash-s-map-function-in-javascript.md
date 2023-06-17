# How can I use Lodash's map function in JavaScript?
// plain

Lodash's `map` function can be used to iterate over an array or object and apply a transformation to each element. It is a convenient way to perform a common operation on a collection of data.

Here is an example of using `map` to double the values of an array of numbers:

```
const numbers = [1, 2, 3, 4, 5];

const doubled = _.map(numbers, (num) => {
  return num * 2;
});

console.log(doubled);
// Output: [2, 4, 6, 8, 10]
```

In this example:

1. `numbers` is an array of numbers that we want to double.
2. `doubled` is a new array that we will create by mapping over the original array.
3. `_.map` is the Lodash map function that will iterate over the array and apply the transformation.
4. The transformation is a function that takes a single argument `num` and returns the result of multiplying it by 2.

## Helpful links

- [Lodash Documentation: `map`](https://lodash.com/docs/4.17.15#map)
- [MDN Documentation: `Array.prototype.map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

onelinerhub: [How can I use Lodash's map function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-map-function-in-javascript)