# How can I use Lodash's extend() function in JavaScript?
// plain

The Lodash `extend()` function is a utility method that allows you to merge two or more objects together. It takes in any number of objects as arguments and returns a new object containing all the properties of the objects passed in.

For example, the following code creates two objects and then merges them together using `extend()`:

```
var object1 = {
  name: 'John',
  age: 30
};

var object2 = {
  job: 'Software Engineer',
  city: 'New York'
};

var mergedObject = _.extend(object1, object2);
```

The output of this code is:

```
{
  name: 'John',
  age: 30,
  job: 'Software Engineer',
  city: 'New York'
}
```

The `extend()` function works by iterating over each of the objects passed in and copying all of their properties into the new object. If two objects have the same property name, the property from the last object passed in will take precedence.

Here is a breakdown of the code above:

- `var object1 = { name: 'John', age: 30 };`: This creates an object with two properties, `name` and `age`.
- `var object2 = { job: 'Software Engineer', city: 'New York' };`: This creates an object with two properties, `job` and `city`.
- `var mergedObject = _.extend(object1, object2);`: This uses the `extend()` function to merge the two objects together.

For more information on Lodash's `extend()` function, please refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#extend).

onelinerhub: [How can I use Lodash's extend() function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-extend---function-in-javascript)