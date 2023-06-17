# How can I use Lodash to compare two arrays of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to compare two arrays of objects in JavaScript using the `_.isEqual()` method.

## Example code

```javascript
let array1 = [{name: 'Bob', age: 20}, {name: 'John', age: 30}];
let array2 = [{name: 'Bob', age: 20}, {name: 'John', age: 30}];

console.log(_.isEqual(array1, array2));
```

## Output example

```
true
```

The `_.isEqual()` method takes two arrays as parameters and returns `true` if their values are the same, and `false` otherwise. In this example, the two arrays are identical, so the method returns `true`.

## Code explanation


- `let array1 = [{name: 'Bob', age: 20}, {name: 'John', age: 30}];` - This creates an array of objects with two elements. Each element has a `name` and `age` property.
- `let array2 = [{name: 'Bob', age: 20}, {name: 'John', age: 30}];` - This creates a second array of objects with two elements. The values of the elements are the same as the first array.
- `console.log(_.isEqual(array1, array2));` - This uses the Lodash `_.isEqual()` method to compare the two arrays. It takes two parameters, which are the two arrays, and returns `true` if the values are the same, and `false` otherwise.

## Helpful links

- Lodash Documentation: https://lodash.com/docs/
- `_.isEqual()` Documentation: https://lodash.com/docs/#isEqual

onelinerhub: [How can I use Lodash to compare two arrays of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-compare-two-arrays-of-objects-in-javascript)