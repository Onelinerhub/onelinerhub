# How do I use the lodash get method in JavaScript?
// plain

The lodash get method in JavaScript is used to retrieve a value from an object given a path. It is useful for accessing deeply nested properties without having to check for undefined values.

## Example


```
const _ = require('lodash');

const obj = {
  a: {
    b: {
      c: 'value'
    }
  }
};

const value = _.get(obj, 'a.b.c');

console.log(value);
// Output: 'value'
```

The code above uses the lodash get method to retrieve the value of the property `c` in the object `obj`. The first argument of the get method is the object, and the second argument is a path string that indicates the property to be retrieved.

Parts of the code:
- `require('lodash')`: This statement imports the lodash library.
- `_.get(obj, 'a.b.c')`: This statement uses the get method to retrieve the value of the property `c` in the object `obj`.
- `console.log(value)`: This statement prints the retrieved value to the console.

## Helpful links
- [Lodash API Documentation](https://lodash.com/docs/4.17.15)
- [How to Use Lodash's get Method](https://medium.com/@dmitriy.korobitsyn/how-to-use-lodashs-get-method-9f3ff9c2f6f3)

onelinerhub: [How do I use the lodash get method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-the-lodash-get-method-in-javascript)