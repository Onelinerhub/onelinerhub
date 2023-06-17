# How do I use Lodash to set values in JavaScript?
// plain

Lodash is a JavaScript library that helps simplify common programming tasks. It can be used to set values in JavaScript in a few different ways.

1. Using the `set` method:
```javascript
const _ = require('lodash');

let obj = {};

_.set(obj, 'a.b.c', 10);

console.log(obj);
// { a: { b: { c: 10 } } }
```
The `set` method takes an object, a property path, and a value. It will then set the value to the property path specified.

2. Using the `update` method:
```javascript
const _ = require('lodash');

let obj = { a: { b: { c: 5 } } };

_.update(obj, 'a.b.c', n => n * 2);

console.log(obj);
// { a: { b: { c: 10 } } }
```
The `update` method takes an object, a property path, and a function. It will then update the value at the property path with the result of the function.

These are just two of the ways that Lodash can be used to set values in JavaScript. For more information, see the [Lodash documentation](https://lodash.com/docs/).

onelinerhub: [How do I use Lodash to set values in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-set-values-in-javascript-1687011312)