# How can I compare the usage of lodash's foreach to the native JavaScript foreach loop?
// plain

Lodash's `_.forEach()` and native JavaScript's `forEach()` are both methods used to iterate through arrays.

The main difference between the two is that Lodash's `_.forEach()` method is faster and more efficient than the native `forEach()` method.

For example:

```javascript
// Native forEach()
const arr = [1,2,3];
arr.forEach(el => console.log(el));
// Output: 1 2 3

// Lodash _.forEach()
const arr = [1,2,3];
_.forEach(arr, el => console.log(el));
// Output: 1 2 3
```

The code above shows the same output when using either `forEach()` method.

However, Lodash's `_.forEach()` method is slightly faster and more efficient as it has additional features such as being able to break out of a loop, handle exceptions, and provide more control over iteration.

## Code explanation

* `const arr = [1,2,3];` - declaring an array of numbers
* `arr.forEach(el => console.log(el));` - using the native `forEach()` method to iterate through the array and log each element to the console
* `_.forEach(arr, el => console.log(el));` - using Lodash's `_.forEach()` method to iterate through the array and log each element to the console

List of ## Helpful links
* [MDN - forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
* [Lodash - _.forEach()](https://lodash.com/docs/4.17.15#forEach)

onelinerhub: [How can I compare the usage of lodash's foreach to the native JavaScript foreach loop?](https://onelinerhub.com/javascript-lodash/how-can-i-compare-the-usage-of-lodash-s-foreach-to-the-native-javascript-foreach-loop)