# How can I use Lodash to remove duplicates from an array in JavaScript?
// plain

Using Lodash, you can easily remove duplicates from an array in JavaScript. Here is an example:

```
const array = [1, 2, 3, 3, 4, 5, 6, 6];

const uniqueArray = _.uniq(array);

console.log(uniqueArray);
// Output: [1, 2, 3, 4, 5, 6]
```

The code above uses the `_.uniq()` Lodash method to remove duplicates from the `array` variable. This method takes an array as an argument and returns a new array with only unique values.

## Code explanation


- `const array = [1, 2, 3, 3, 4, 5, 6, 6];`: This creates an array with duplicate values.
- `const uniqueArray = _.uniq(array);`: This uses the `_.uniq()` Lodash method to remove duplicates from the `array` variable.
- `console.log(uniqueArray);`: This prints the new array with unique values to the console.

For more information, check out the [Lodash documentation](https://lodash.com/docs/).

onelinerhub: [How can I use Lodash to remove duplicates from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-duplicates-from-an-array-in-javascript)