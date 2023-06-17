# How can I use Lodash's reject function in JavaScript?
// plain

The `reject` function in Lodash is used to filter out items in an array that meet certain criteria. It takes an array and a predicate (function that returns true or false) as arguments and returns a new array with the items that do not meet the criteria.

For example:
```
const _ = require('lodash');

const numbers = [1, 2, 3, 4, 5];

const oddNumbers = _.reject(numbers, (num) => {
  return num % 2 === 0;
});

console.log(oddNumbers);
// Output: [1, 3, 5]
```

In the example above, `_.reject` takes an array of numbers, and a predicate that checks if the number is even. The `reject` function then returns a new array with all the odd numbers from the original array.

The parts of the example above are:
1. `const _ = require('lodash');` - This imports the Lodash library.
2. `const numbers = [1, 2, 3, 4, 5];` - This is the original array of numbers.
3. `const oddNumbers = _.reject(numbers, (num) => {` - This is the call to the `reject` function, which takes two arguments - the array and a predicate.
4. `return num % 2 === 0;` - This is the predicate, which checks if the number is even.
5. `console.log(oddNumbers);` - This prints out the new array with all the odd numbers.

For more information about Lodash's `reject` function, see [the official documentation](https://lodash.com/docs/4.17.15#reject).

onelinerhub: [How can I use Lodash's reject function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-reject-function-in-javascript)