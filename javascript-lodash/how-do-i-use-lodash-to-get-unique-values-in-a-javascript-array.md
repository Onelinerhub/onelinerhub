# How do I use Lodash to get unique values in a JavaScript array?
// plain

Using Lodash, you can easily get unique values from a JavaScript array. Here is an example:

```
// Import Lodash
const _ = require('lodash');

// Create an array
let arr = [1, 2, 2, 3, 4, 4, 5];

// Get unique values
let unique = _.uniq(arr);
console.log(unique); // Output: [1, 2, 3, 4, 5]
```

The code above uses Lodash's `uniq()` method to get unique values from the array `arr`. The output is an array containing only the unique values: `[1, 2, 3, 4, 5]`.

The `uniq()` method takes an array as an argument and returns a new array with only the unique values from the original array.

## Code explanation

- `require('lodash')`: This imports the Lodash library.
- `_.uniq(arr)`: This is the Lodash method used to get unique values from an array.
- `console.log(unique)`: This prints the result of the `uniq()` method to the console.

Here are some ## Helpful links
- [Lodash](https://lodash.com/)
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [uniq() Method](https://lodash.com/docs/4.17.15#uniq)

onelinerhub: [How do I use Lodash to get unique values in a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-get-unique-values-in-a-javascript-array)