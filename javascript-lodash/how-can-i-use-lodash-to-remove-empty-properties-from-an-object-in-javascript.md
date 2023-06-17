# How can I use Lodash to remove empty properties from an object in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of these tasks is removing empty properties from an object. This can be done using the _.omit() method.

```
const object = {
  name: 'John',
  age: '',
  address: '123 Main Street'
};

const result = _.omit(object, ['age']);
console.log(result);
```
## Output example

```
{ name: 'John', address: '123 Main Street' }
```

The _.omit() method takes two arguments: the object and an array of keys to omit. In the example above, we pass in the object and an array with the key `age` to omit. The result is a new object without the `age` property.

The _.omit() method is just one of many Lodash methods that can be used to manipulate objects. For more information, see the [Lodash documentation](https://lodash.com/docs/).

onelinerhub: [How can I use Lodash to remove empty properties from an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-empty-properties-from-an-object-in-javascript)