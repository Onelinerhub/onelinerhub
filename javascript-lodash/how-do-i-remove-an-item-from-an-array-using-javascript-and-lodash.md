# How do I remove an item from an array using JavaScript and Lodash?
// plain

Removing an item from an array using JavaScript and Lodash is a fairly straightforward task. The _.pull() method is the most common way to do this. It takes an array and one or more values, and removes all occurrences of the values from the array.

For example, if you have an array `arr` with the elements `[1, 2, 3, 4, 5]`, you can use `_.pull()` to remove the value `3` from it:

```
const arr = [1, 2, 3, 4, 5];
_.pull(arr, 3);
console.log(arr); // [1, 2, 4, 5]
```

The `_.pull()` method also accepts multiple values, allowing you to remove multiple items from an array at once. For example, if you have an array `arr` with the elements `[1, 2, 3, 4, 5]`, you can use `_.pull()` to remove the values `3` and `4` from it:

```
const arr = [1, 2, 3, 4, 5];
_.pull(arr, 3, 4);
console.log(arr); // [1, 2, 5]
```

The `_.pull()` method is part of the [Lodash](https://lodash.com/) library, and can be used in both Node.js and browser environments.

## Code explanation

- `const arr = [1, 2, 3, 4, 5];`: This line creates an array with the elements `[1, 2, 3, 4, 5]`.
- `_.pull(arr, 3);`: This line uses the `_.pull()` method to remove the value `3` from the array `arr`.
- `_.pull(arr, 3, 4);`: This line uses the `_.pull()` method to remove the values `3` and `4` from the array `arr`.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)

onelinerhub: [How do I remove an item from an array using JavaScript and Lodash?](https://onelinerhub.com/javascript-lodash/how-do-i-remove-an-item-from-an-array-using-javascript-and-lodash)