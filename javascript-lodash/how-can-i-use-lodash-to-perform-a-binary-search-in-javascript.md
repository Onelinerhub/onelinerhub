# How can I use Lodash to perform a binary search in JavaScript?
// plain

Using Lodash, you can perform a binary search in JavaScript by using the `_.sortedIndex()` function. This function takes an array and a value as parameters and returns the index at which the value should be inserted into the array in order to maintain its sort order.

## Example code

```js
const arr = [1, 2, 4, 5, 7, 9, 10];
const value = 6;

const index = _.sortedIndex(arr, value);
console.log(index);
```

## Output example

```
4
```

The code above searches for the index of the value `6` in the sorted array `[1, 2, 4, 5, 7, 9, 10]` using `_.sortedIndex()`. The output is `4`, meaning that the value `6` should be inserted at index `4` for the array to remain sorted.

## Code explanation

* `const arr = [1, 2, 4, 5, 7, 9, 10];` - declares an array of sorted numbers
* `const value = 6;` - declares the value to search for in the array
* `const index = _.sortedIndex(arr, value);` - uses Lodash's `_.sortedIndex()` function to search for the index of the value in the array
* `console.log(index);` - prints the index of the value in the array

## Helpful links
* [Lodash Documentation - _.sortedIndex()](https://lodash.com/docs/4.17.15#sortedIndex)

onelinerhub: [How can I use Lodash to perform a binary search in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-perform-a-binary-search-in-javascript)