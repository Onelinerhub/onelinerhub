# How can I use Lodash to get the path of a nested object in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of those tasks is getting the path of a nested object in JavaScript. This can be done by using the `_.get()` method.

```javascript
const obj = {
  a: {
    b: {
      c: 'value'
    }
  }
}

const path = _.get(obj, 'a.b.c');

console.log(path);
// Output: 'value'
```

The `_.get()` method takes two arguments: the object to be searched and the path of the property to be retrieved. In the example above, `obj` is the object to be searched and `'a.b.c'` is the path of the property to be retrieved. The `_.get()` method will then traverse the object and return the value of the property at the specified path.

## Code explanation


- `const obj = { a: { b: { c: 'value' } } }`: This is the object to be searched.
- `const path = _.get(obj, 'a.b.c')`: This is the call to the `_.get()` method, which takes two arguments: the object to be searched and the path of the property to be retrieved.
- `console.log(path)`: This will print the value of the property at the specified path.

## Helpful links

- [Lodash documentation](https://lodash.com/docs/)
- [_.get() method documentation](https://lodash.com/docs/4.17.15#get)

onelinerhub: [How can I use Lodash to get the path of a nested object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-get-the-path-of-a-nested-object-in-javascript)