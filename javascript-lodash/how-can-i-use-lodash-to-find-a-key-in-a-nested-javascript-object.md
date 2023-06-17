# How can I use Lodash to find a key in a nested JavaScript object?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to find a key in a nested JavaScript object.

The `_.get()` function can be used to traverse the object and return the value of the key. It takes three arguments: the object, the path of the key, and a default value.

## Example

```
const data = {
  a: {
    b: {
      c: 'foo'
    }
  }
};

const value = _.get(data, 'a.b.c', 'default');

console.log(value);
// Output: 'foo'
```

In the example above, `data` is the object, `'a.b.c'` is the path of the key, and `'default'` is the default value. The `_.get()` function will return the value of the key `'c'`, which is `'foo'`.

The `_.get()` function is useful for finding a key in a nested JavaScript object.

Parts of code:

- `const data = { ... }`: this is the object containing the nested keys
- `const value = _.get(data, 'a.b.c', 'default')`: this is the `_.get()` function call, which takes the object, the path of the key, and a default value
- `console.log(value)`: this logs the value of the key to the console

## Helpful links
- [Lodash Documentation - _.get()](https://lodash.com/docs/4.17.15#get)

onelinerhub: [How can I use Lodash to find a key in a nested JavaScript object?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-a-key-in-a-nested-javascript-object)