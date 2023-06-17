# How do I use Lodash's pick() method in JavaScript?
// plain

The Lodash `pick()` method is a convenient way to extract certain properties from an object. It takes an object and a list of property names as parameters and returns a new object containing only the specified properties.

For example:

```
const person = {
  name: 'John',
  age: 40,
  occupation: 'Software Engineer'
};

const personData = _.pick(person, ['name', 'age']);

console.log(personData);
```

The output of the above code would be:

```
{
  name: 'John',
  age: 40
}
```

The code works as follows:

1. The `person` object is created with three properties.
2. The `personData` variable is assigned the result of the `_.pick()` method, which takes two parameters - the `person` object and an array of property names.
3. The `_.pick()` method returns a new object containing only the specified properties.

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15#pick).

onelinerhub: [How do I use Lodash's pick() method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-pick---method-in-javascript)