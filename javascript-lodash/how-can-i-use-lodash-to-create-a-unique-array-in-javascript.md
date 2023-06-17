# How can I use Lodash to create a unique array in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of the functions that Lodash provides is `_.uniq()`, which can be used to create a unique array in JavaScript.

Here is an example of how to use `_.uniq()` to create a unique array:

```js
const arr = [1, 2, 3, 1, 2, 3];
const uniqueArr = _.uniq(arr);

console.log(uniqueArr); // [1, 2, 3]
```

The `_.uniq()` function takes an array as an argument and returns a new array with the unique values from the original array.

The code is composed of the following parts:

1. `const arr = [1, 2, 3, 1, 2, 3];`: This declares a variable `arr` and assigns it to an array with duplicate values.

2. `const uniqueArr = _.uniq(arr);`: This declares a variable `uniqueArr` and assigns it to the result of calling `_.uniq()` with the `arr` array as an argument.

3. `console.log(uniqueArr);`: This logs the `uniqueArr` array to the console.

For more information, see the [Lodash Documentation](https://lodash.com/docs/).

onelinerhub: [How can I use Lodash to create a unique array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-create-a-unique-array-in-javascript)