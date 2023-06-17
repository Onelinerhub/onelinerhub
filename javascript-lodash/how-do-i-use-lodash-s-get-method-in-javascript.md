# How do I use Lodash's get method in JavaScript?
// plain

Lodash's `get` method is a convenient way to retrieve a value from an object. It allows you to safely access a property on an object without having to worry about TypeErrors.

For example:

```
const person = {
  name: 'John Doe',
  age: 25
};

const name = _.get(person, 'name');
console.log(name); // 'John Doe'
```

In this example, `_.get` is used to retrieve the `name` property from the `person` object.

The `_.get` method takes two arguments: the object to retrieve the value from, and the path to the property. If the property is deeply nested within the object, the path can be a string of dot-separated keys.

For example:

```
const person = {
  name: {
    first: 'John',
    last: 'Doe'
  },
  age: 25
};

const firstName = _.get(person, 'name.first');
console.log(firstName); // 'John'
```

The `_.get` method can also take a third argument, a default value, which will be returned if the specified property is not found.

For example:

```
const person = {
  name: 'John Doe',
  age: 25
};

const middleName = _.get(person, 'name.middle', 'N/A');
console.log(middleName); // 'N/A'
```

For more information, see the [Lodash Documentation](https://lodash.com/docs/4.17.15#get).

onelinerhub: [How do I use Lodash's get method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-get-method-in-javascript)