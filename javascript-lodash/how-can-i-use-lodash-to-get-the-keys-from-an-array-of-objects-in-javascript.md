# How can I use Lodash to get the keys from an array of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides many utility functions for working with objects and arrays. It can be used to get the keys from an array of objects in JavaScript.

The `_.keys()` function takes in an object and returns an array of the keys of the object.

## Example


```
const arr = [
  { a: 1, b: 2 },
  { c: 3, d: 4 },
  { e: 5, f: 6 }
]

const keys = _.keys(arr);

console.log(keys);
```

## Output example

```
[0, 1, 2]
```

The code above uses the `_.keys()` function to get the keys from the array of objects `arr`. The result is an array of the keys of the objects in the array (in this case, `[0, 1, 2]`).

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15).

onelinerhub: [How can I use Lodash to get the keys from an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-get-the-keys-from-an-array-of-objects-in-javascript)