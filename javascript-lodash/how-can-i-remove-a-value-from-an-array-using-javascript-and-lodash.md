# How can I remove a value from an array using JavaScript and Lodash?
// plain

Removing a value from an array using JavaScript and Lodash can be done using the `_.pull()` method. This method takes two arguments: an array and a value to remove. The value can be a primitive or an object. The following example code shows how to use `_.pull()` to remove the value `2` from an array of numbers:

```
const numbers = [1, 2, 3];
_.pull(numbers, 2);
console.log(numbers); // [1, 3]
```

The `_.pull()` method modifies the array in-place and returns the modified array.

The `_.pullAll()` method can be used to remove multiple values from an array. This method takes two arguments: an array and an array of values to remove. The following example code shows how to use `_.pullAll()` to remove the values `2` and `3` from an array of numbers:

```
const numbers = [1, 2, 3];
_.pullAll(numbers, [2, 3]);
console.log(numbers); // [1]
```

The `_.pullAll()` method also modifies the array in-place and returns the modified array.

## Code explanation
**

1. `_.pull()`: Takes two arguments: an array and a value to remove
2. `_.pullAll()`: Takes two arguments: an array and an array of values to remove

**## Helpful links**

- [Lodash Documentation - _.pull()](https://lodash.com/docs/4.17.15#pull)
- [Lodash Documentation - _.pullAll()](https://lodash.com/docs/4.17.15#pullAll)

onelinerhub: [How can I remove a value from an array using JavaScript and Lodash?](https://onelinerhub.com/javascript-lodash/how-can-i-remove-a-value-from-an-array-using-javascript-and-lodash)