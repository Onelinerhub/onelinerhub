# How can I use Lodash to remove undefined values from an object in JavaScript?
// plain

Lodash provides a utility function `_.omitBy` to remove undefined values from an object. The following example code will demonstrate how to use it:

```
const _ = require('lodash');

const obj = {
  a: 'hello',
  b: undefined,
  c: 'world'
};

const modified = _.omitBy(obj, _.isUndefined);
console.log(modified);
```

## Output example


```
{ a: 'hello', c: 'world' }
```

The code does the following:

1. `require`s the lodash library.
2. Creates an object `obj` with two defined and one undefined property.
3. Uses `_.omitBy` to remove all properties with an undefined value.
4. `console.log`s the modified object.

## Helpful links

- [Lodash Documentation for _.omitBy](https://lodash.com/docs/4.17.15#omitBy)
- [MDN Documentation for isUndefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)

onelinerhub: [How can I use Lodash to remove undefined values from an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-undefined-values-from-an-object-in-javascript)