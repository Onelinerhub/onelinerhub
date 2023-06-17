# How can I use lodash's `some()` method to achieve the same result as the JavaScript `some()` method?
// plain

The `some()` method from Lodash is a collection method which is used to check if at least one element in the collection passes the given predicate. It is similar to the native JavaScript `some()` method, but it has a few extra features.

Here is an example of how to use the `some()` method from Lodash to achieve the same result as the native JavaScript `some()` method:

```javascript
const array = [1, 2, 3];

const result = _.some(array, (element) => {
  return element > 2;
});

console.log(result); // true
```

The code above consists of the following parts:

1. The `array` variable is initialized with an array of numbers.
2. The `some()` method is called on the `array` variable, passing a predicate as a parameter. The predicate checks if an element is greater than 2.
3. The `result` variable stores the result of the `some()` method call.
4. The `console.log()` method is called to display the result.

The output of the code above is `true`, as at least one element in the array is greater than 2.

## Helpful links

- [Lodash `some()` docs](https://lodash.com/docs/4.17.15#some)
- [MDN `some()` docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)

onelinerhub: [How can I use lodash's `some()` method to achieve the same result as the JavaScript `some()` method?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s--some----method-to-achieve-the-same-result-as-the-javascript--some----method)