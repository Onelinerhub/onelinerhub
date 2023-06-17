# How can I use Lodash to deep compare two arrays of objects in JavaScript?
// plain

Lodash is a JavaScript utility library that provides many helpful functions for manipulating and working with objects and arrays. One of the utility functions Lodash provides is the `_.isEqual()` function. This function can be used to deep compare two arrays of objects in JavaScript.

## Example code

```javascript
const array1 = [
  {
    id: 1,
    name: 'John',
  },
  {
    id: 2,
    name: 'Jane',
  },
];

const array2 = [
  {
    id: 1,
    name: 'John',
  },
  {
    id: 2,
    name: 'Jane',
  },
];

console.log(_.isEqual(array1, array2));
```

## Output example

```
true
```

The code above uses the `_.isEqual()` function to deep compare two arrays of objects. The function compares each item in the two arrays and returns `true` if the objects are equal and `false` if they are not equal.

## Code explanation

- `const array1`: declares a variable named `array1` and assigns it an array of objects.
- `const array2`: declares a variable named `array2` and assigns it an array of objects.
- `_.isEqual()`: the Lodash function used to deep compare two arrays of objects.
- `console.log()`: prints the result of the comparison to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [_.isEqual() Documentation](https://lodash.com/docs/4.17.15#isEqual)

onelinerhub: [How can I use Lodash to deep compare two arrays of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-deep-compare-two-arrays-of-objects-in-javascript)