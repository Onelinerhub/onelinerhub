# How do I use Lodash to remove elements from an array in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to remove elements from an array in JavaScript by using the `_.pull()` method. This method takes an array and one or more values as arguments and removes all instances of those values from the array.

For example, given the following array:

```
const array = [1, 2, 3, 4, 5, 3, 6];
```

We can use `_.pull()` to remove all instances of 3 from the array:

```
_.pull(array, 3);
```

The result will be:

```
[1, 2, 4, 5, 6]
```

## Code explanation


- `_.pull()`: The Lodash method used to remove elements from an array.
- `array`: The array from which elements are removed.
- `3`: The value of the element to be removed.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

onelinerhub: [How do I use Lodash to remove elements from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-elements-from-an-array-in-javascript)