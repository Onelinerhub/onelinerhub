# How can I use Lodash to find a key in an object in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to find a key in an object in JavaScript.

For example, if you have an object `user` with the following structure:

```
const user = {
  name: 'John',
  age: 30
}
```

You can use Lodash's `_.has()` method to check if the object has a certain key, in this case `name`, like this:

```
_.has(user, 'name');
// Output: true
```

The `_.has()` method takes two arguments:

1. The object to check
2. The key to check for

It then returns `true` if the key exists in the object, or `false` if it does not.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [_.has() Method](https://lodash.com/docs/4.17.15#has)

onelinerhub: [How can I use Lodash to find a key in an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-a-key-in-an-object-in-javascript)