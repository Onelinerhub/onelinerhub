# How do I use lodash's concat function in JavaScript?
// plain

The `concat` function provided by lodash is a powerful tool for combining two arrays into one. It can be used in JavaScript as follows:

```
// Create two arrays to be combined
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

// Use lodash's concat function to combine the two arrays
let combinedArr = _.concat(arr1, arr2);

console.log(combinedArr); // [1, 2, 3, 4, 5, 6]
```

The `concat` function takes two arguments, both of which must be arrays. The first argument is the base array, and the second argument is the array that will be appended to the base array. The function returns the combined array.

## Code explanation


* `let arr1 = [1, 2, 3];` - This line creates an array with three elements.
* `let arr2 = [4, 5, 6];` - This line creates a second array with three elements.
* `let combinedArr = _.concat(arr1, arr2);` - This line uses the `concat` function provided by lodash to combine the two arrays.
* `console.log(combinedArr);` - This line prints the combined array to the console.

For more information on lodash's `concat` function, see [here](https://lodash.com/docs/4.17.15#concat).

onelinerhub: [How do I use lodash's concat function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-concat-function-in-javascript)