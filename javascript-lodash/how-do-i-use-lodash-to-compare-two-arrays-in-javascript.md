# How do I use Lodash to compare two arrays in JavaScript?
// plain

Lodash is a JavaScript library that provides many utility functions for manipulating and working with objects. One of the functions it provides is `_.isEqual()`, which can be used to compare two arrays in JavaScript.

The `_.isEqual()` function takes two arguments and returns a boolean value indicating whether the two arguments are equal or not. Here is an example of how to use `_.isEqual()` to compare two arrays:

```
let arr1 = [1, 2, 3];
let arr2 = [1, 2, 3];

console.log(_.isEqual(arr1, arr2));
```

## Output example

```
true
```

The code above does the following:

1. Defines two arrays `arr1` and `arr2` with the same values.
2. Calls the `_.isEqual()` function, passing in `arr1` and `arr2` as arguments.
3. The `_.isEqual()` function returns a boolean value indicating whether the two arguments are equal or not. In this case, it returns `true` since the two arrays are equal.

For more information on Lodash and the `_.isEqual()` function, see the [Lodash documentation](https://lodash.com/docs/4.17.15).

onelinerhub: [How do I use Lodash to compare two arrays in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-compare-two-arrays-in-javascript)