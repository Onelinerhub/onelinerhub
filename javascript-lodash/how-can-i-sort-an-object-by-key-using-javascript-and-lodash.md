# How can I sort an object by key using JavaScript and Lodash?
// plain

Using Lodash, you can sort an object by key using the `_.sortBy()` method. This method takes an object as its first argument, and an iteratee function as its second argument. The iteratee function is used to determine the order of the returned array.

For example, this code will sort an object by its keys in ascending order:

```
const object = {
  c: 3,
  a: 1,
  b: 2
};

const sortedObject = _.sortBy(object, (value, key) => key);

console.log(sortedObject);
// Output: { a: 1, b: 2, c: 3 }
```

The code is composed of the following parts:

1. `const object = { c: 3, a: 1, b: 2 };` - this declares an object with 3 key-value pairs.

2. `const sortedObject = _.sortBy(object, (value, key) => key);` - this calls the `_.sortBy()` method on the `object` variable, passing an iteratee function as the second argument. This iteratee function takes the `value` and `key` arguments, and returns the `key` argument, which is used to sort the array in ascending order.

3. `console.log(sortedObject);` - this logs the sorted object to the console.

4. `// Output: { a: 1, b: 2, c: 3 }` - this is the output of the code.

## Helpful links

- [Lodash Documentation - _.sortBy()](https://lodash.com/docs/4.17.15#sortBy)
- [MDN Documentation - Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

onelinerhub: [How can I sort an object by key using JavaScript and Lodash?](https://onelinerhub.com/javascript-lodash/how-can-i-sort-an-object-by-key-using-javascript-and-lodash)