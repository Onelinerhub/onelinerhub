# How do I use Lodash to zip two JavaScript arrays together?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of its functions is `_.zip`, which can be used to zip two arrays together.

```
const array1 = ['a', 'b', 'c'];
const array2 = [1, 2, 3];

const zippedArray = _.zip(array1, array2);

console.log(zippedArray);
```

## Output example

```
[
  ['a', 1],
  ['b', 2],
  ['c', 3]
]
```

The `_.zip` function takes two arrays as arguments and returns a new array of arrays, where each inner array contains the elements from the corresponding index of each array.

In the example above, `array1` contains the elements `'a'`, `'b'`, `'c'` and `array2` contains the elements `1`, `2`, `3`. The resulting `zippedArray` contains the elements `['a', 1]`, `['b', 2]`, `['c', 3]`.

## Helpful links
- [Lodash Documentation - _.zip](https://lodash.com/docs/4.17.15#zip)

onelinerhub: [How do I use Lodash to zip two JavaScript arrays together?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-zip-two-javascript-arrays-together)