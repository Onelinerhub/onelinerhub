# How do I use Lodash to remove empty objects from an array in JavaScript?
// plain

Using Lodash, you can remove empty objects from an array in JavaScript using the `_.compact()` method. This method creates a new array with all falsey values removed. Falsey values include `null`, `undefined`, `''`, `false`, `0`, and `NaN`.

For example:

```
const array = [{}, {name: 'John'}, {}, {name: 'Mary'}, {}, null, 0];

const compactArray = _.compact(array);

console.log(compactArray);
// Output: [{name: 'John'}, {name: 'Mary'}]
```

The `_.compact()` method takes an array as an argument and returns a new array with all falsey values removed. In this example, the falsey values include the empty objects and `null`, `0`, which are all removed from the array.

## Code explanation

- `_.compact()`: Lodash method to remove falsey values from an array
- `array`: The array containing objects and falsey values
- `compactArray`: The new array with all falsey values removed

## Helpful links
- [Lodash Documentation: _.compact()](https://lodash.com/docs/4.17.15#compact)

onelinerhub: [How do I use Lodash to remove empty objects from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-empty-objects-from-an-array-in-javascript)