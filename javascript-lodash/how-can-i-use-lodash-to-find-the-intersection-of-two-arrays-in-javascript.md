# How can I use Lodash to find the intersection of two arrays in JavaScript?
// plain

Lodash is a JavaScript library that provides helpful utility functions for common tasks. One of these functions is the `_.intersection()` method, which can be used to find the intersection of two arrays in JavaScript.

The `_.intersection()` method takes two arrays as arguments and returns a new array containing the elements that exist in both arrays. Here is an example:

```javascript
const array1 = [1, 2, 3, 4];
const array2 = [3, 4, 5, 6];

const intersection = _.intersection(array1, array2);

console.log(intersection); // [3, 4]
```

The `_.intersection()` method will compare each element of the two arrays and will return a new array containing the elements that exist in both arrays.

Here are the parts of the example code and their explanations:

- `const array1 = [1, 2, 3, 4];` - This is the first array.
- `const array2 = [3, 4, 5, 6];` - This is the second array.
- `const intersection = _.intersection(array1, array2);` - This is where we call the `_.intersection()` method with the two arrays as arguments and store the returned array in a variable.
- `console.log(intersection);` - This is where we log the returned array to the console.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs)
- [MDN - Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

onelinerhub: [How can I use Lodash to find the intersection of two arrays in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-the-intersection-of-two-arrays-in-javascript)