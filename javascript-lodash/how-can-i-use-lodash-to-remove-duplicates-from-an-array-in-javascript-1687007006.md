# How can I use Lodash to remove duplicates from an array in JavaScript?
// plain

Lodash provides a convenient way to remove duplicates from an array in JavaScript. Here is an example of how it can be done:

```
const _ = require('lodash');

const array = [1, 2, 3, 4, 4, 5, 5];

const uniqueArray = _.uniq(array);

console.log(uniqueArray); // Output: [1, 2, 3, 4, 5]
```

The `_.uniq()` method takes an array as an argument and returns an array with only unique values. It uses a strict equality check (`===`) to determine the uniqueness of each element.

## Code explanation


1. `const _ = require('lodash');` - This line imports the Lodash library into the current scope.
2. `const array = [1, 2, 3, 4, 4, 5, 5];` - This line creates an array with duplicate values.
3. `const uniqueArray = _.uniq(array);` - This line uses the `_.uniq()` method to remove duplicates from the `array` and store the result in `uniqueArray`.
4. `console.log(uniqueArray);` - This line prints the `uniqueArray` to the console.

Here are some ## Helpful links

- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN Array.prototype.uniq()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/uniq)

onelinerhub: [How can I use Lodash to remove duplicates from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-duplicates-from-an-array-in-javascript-1687007006)