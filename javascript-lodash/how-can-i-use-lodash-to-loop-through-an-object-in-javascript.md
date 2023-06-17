# How can I use Lodash to loop through an object in JavaScript?
// plain

Lodash is an JavaScript library that provides utility functions for common programming tasks. It can be used to loop through an object in JavaScript. Here is an example of how it can be done:

```
const _ = require('lodash');

const obj = {
  key1: 'value1',
  key2: 'value2',
  key3: 'value3'
};

_.forEach(obj, (value, key) => {
  console.log(key + ': ' + value);
});
```

## Output example

```
key1: value1
key2: value2
key3: value3
```

The code above uses the `forEach` method from Lodash to loop through an object. This method takes two parameters - an object and a callback function. The callback function takes two parameters - the value of the current key and the key itself. The code then prints out the key and its value.

## Code explanation

- `require('lodash')`: imports the Lodash library
- `_.forEach(obj, (value, key) => {`: uses the `forEach` method from Lodash to loop through the object
- `console.log(key + ': ' + value);`: prints out the key and its value

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [How to Loop Through an Object in JavaScript](https://medium.com/javascript-in-plain-english/how-to-loop-through-an-object-in-javascript-fcf10305aaab)

onelinerhub: [How can I use Lodash to loop through an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-loop-through-an-object-in-javascript)