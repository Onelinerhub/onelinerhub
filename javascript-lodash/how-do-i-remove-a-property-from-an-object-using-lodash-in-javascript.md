# How do I remove a property from an object using Lodash in JavaScript?
// plain

Using Lodash, you can remove a property from an object by using the `_.omit()` method. This method accepts two arguments: the object to be modified and the name of the property to be removed. Here is an example:

```
const obj = {
  name: 'John',
  age: 25
};

const result = _.omit(obj, 'age');

console.log(result);
// { name: 'John' }
```

The `_.omit()` method returns a new object, leaving the original object intact. The `result` variable in the example above contains the modified object without the `age` property.

- `obj`: The object to be modified.
- `'age'`: The name of the property to be removed from the object.

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15#omit).

onelinerhub: [How do I remove a property from an object using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-remove-a-property-from-an-object-using-lodash-in-javascript)