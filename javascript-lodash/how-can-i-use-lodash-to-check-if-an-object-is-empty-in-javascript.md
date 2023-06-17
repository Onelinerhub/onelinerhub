# How can I use Lodash to check if an object is empty in Javascript?
// plain

Using Lodash, you can check if an object is empty in Javascript by using the `_.isEmpty()` function. This function takes a single argument, which is the object to check. The function will return `true` if the object is empty, and `false` if the object is not empty.

For example:
```
const object1 = {};
const object2 = {name: 'John'};

console.log(_.isEmpty(object1)); // true
console.log(_.isEmpty(object2)); // false
```
## Output example

```
true
false
```

The `_.isEmpty()` function checks the following conditions to determine if an object is empty:
- If the object is `null`
- If the object is an array with no elements
- If the object is an object with no own enumerable properties

## Helpful links
- [Lodash Documentation for _.isEmpty()](https://lodash.com/docs/4.17.15#isEmpty)

onelinerhub: [How can I use Lodash to check if an object is empty in Javascript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-check-if-an-object-is-empty-in-javascript)