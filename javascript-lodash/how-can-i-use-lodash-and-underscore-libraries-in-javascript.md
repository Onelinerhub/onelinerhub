# How can I use Lodash and Underscore libraries in JavaScript?
// plain

Lodash and Underscore are two popular JavaScript libraries that provide a wide range of utility functions for manipulating and working with data. They are both open source libraries and can be used in any JavaScript application.

Here is an example of how to use Lodash to filter an array of objects:
```
const users = [
  { name: 'John', age: 30 },
  { name: 'Jack', age: 20 },
  { name: 'Jill', age: 40 },
];

const filteredUsers = _.filter(users, user => user.age > 25);

console.log(filteredUsers);
// Output: [{ name: 'John', age: 30 }, { name: 'Jill', age: 40 }]
```

The code above uses the `_.filter` function from Lodash to filter an array of objects based on the given condition. It takes two arguments - the array to filter and the condition to filter by. The result is an array containing only the objects that match the condition.

The same example using Underscore would look like this:
```
const users = [
  { name: 'John', age: 30 },
  { name: 'Jack', age: 20 },
  { name: 'Jill', age: 40 },
];

const filteredUsers = _.filter(users, user => user.age > 25);

console.log(filteredUsers);
// Output: [{ name: 'John', age: 30 }, { name: 'Jill', age: 40 }]
```

Both Lodash and Underscore provide a wide range of utility functions that can be used to manipulate and work with data in JavaScript applications. They are both open source libraries and can be used in any JavaScript application.

## Code explanation

  1. `const users = [{ name: 'John', age: 30 }, { name: 'Jack', age: 20 }, { name: 'Jill', age: 40 }];` - Declaring an array of objects.
  2. `_.filter(users, user => user.age > 25);` - Filtering the array of objects using the `_.filter` function from Lodash.
  3. `console.log(filteredUsers);` - Logging the filtered array to the console.

* ## Helpful links
  * [Lodash Documentation](https://lodash.com/docs/)
  * [Underscore Documentation](http://underscorejs.org/)

onelinerhub: [How can I use Lodash and Underscore libraries in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-and-underscore-libraries-in-javascript)