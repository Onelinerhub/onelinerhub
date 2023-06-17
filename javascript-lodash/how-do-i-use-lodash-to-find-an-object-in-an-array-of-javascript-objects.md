# How do I use Lodash to find an object in an array of JavaScript objects?
// plain

Using Lodash to find an object in an array of JavaScript objects is simple and straightforward. The following example code block shows how to use Lodash's `_.find` method to find an object in an array of JavaScript objects:

```javascript
const users = [{
  'user': 'barney',
  'age': 36
}, {
  'user': 'fred',
  'age': 40
}, {
  'user': 'pebbles',
  'age': 1
}];

const user = _.find(users, { 'age': 36 });

console.log(user);
```

## Output example

```
{
  'user': 'barney',
  'age': 36
}
```

The code above first creates an array of JavaScript objects called `users` and then uses Lodash's `_.find` method to find an object that has an `age` property with the value of 36. The `_.find` method returns the first object in the array that matches the criteria, and in this case it returns the object with `user` property set to `barney` and `age` property set to 36.

## Code explanation

1. `const users = [{...}, {...}, {...}];` - creates an array of JavaScript objects called `users`
2. `const user = _.find(users, { 'age': 36 });` - uses Lodash's `_.find` method to find an object with an `age` property set to 36
3. `console.log(user);` - prints the found object to the console

## Helpful links
- Lodash documentation: https://lodash.com/docs/4.17.15
- `_.find` method documentation: https://lodash.com/docs/4.17.15#find

onelinerhub: [How do I use Lodash to find an object in an array of JavaScript objects?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-find-an-object-in-an-array-of-javascript-objects)