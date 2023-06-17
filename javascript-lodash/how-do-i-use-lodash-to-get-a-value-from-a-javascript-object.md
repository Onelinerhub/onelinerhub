# How do I use Lodash to get a value from a JavaScript object?
// plain

Lodash provides a convenient way to get a value from a JavaScript object. Here is an example of how to use Lodash to get a value from a JavaScript object:

```
const _ = require('lodash');
const obj = {
  name: 'John',
  age: 25
};

const name = _.get(obj, 'name');
console.log(name); // Output: John
```

1. `const _ = require('lodash');` - This line imports the Lodash library so that it can be used in the program.
2. `const obj = { name: 'John', age: 25 };` - This creates an object with two properties, `name` and `age`.
3. `const name = _.get(obj, 'name');` - This line uses Lodash's `get()` method to get the value of the `name` property from the `obj` object.
4. `console.log(name);` - This line prints the value of the `name` property to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [MDN Web Docs - Object.get](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/get)

onelinerhub: [How do I use Lodash to get a value from a JavaScript object?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-get-a-value-from-a-javascript-object)