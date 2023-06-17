# How do I use Lodash to merge two arrays in JavaScript?
// plain

Using Lodash to merge two arrays in JavaScript is easy. Here's an example code block to show how it works:

```
const _ = require('lodash');

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const mergedArray = _.concat(array1, array2);

console.log(mergedArray); // Output: [1, 2, 3, 4, 5, 6]
```

The code above uses the `_.concat()` method from Lodash to merge two arrays together. It takes two arguments, the two arrays to be merged, and returns a new array containing the elements of both arrays.

## Code explanation


- `const _ = require('lodash');` - This line imports the Lodash library into the code.
- `const array1 = [1, 2, 3];` - This line creates the first array.
- `const array2 = [4, 5, 6];` - This line creates the second array.
- `const mergedArray = _.concat(array1, array2);` - This line uses the `_.concat()` method to merge the two arrays together and store the result in a new variable.
- `console.log(mergedArray);` - This line logs the result of the merge to the console.

Here are some ## Helpful links

- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN Array.concat() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)

onelinerhub: [How do I use Lodash to merge two arrays in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-merge-two-arrays-in-javascript)