# How can I use Lodash to group an array of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of its most useful features is the _.groupBy() method, which allows you to group an array of objects based on a given property.

For example, let's say we have an array of objects that each represent a person and contain their name and age:

```javascript
const people = [
  { name: 'John', age: 20 },
  { name: 'Jane', age: 30 },
  { name: 'Jack', age: 20 },
  { name: 'Jill', age: 30 }
];
```

Using Lodash's _.groupBy() method, we can group these objects by age:

```javascript
const groupedPeople = _.groupBy(people, 'age');
```

This will return an object with two keys, one for each age, containing an array of objects representing the people with that age:

```javascript
{
  20: [
    { name: 'John', age: 20 },
    { name: 'Jack', age: 20 }
  ],
  30: [
    { name: 'Jane', age: 30 },
    { name: 'Jill', age: 30 }
  ]
}
```

In summary, Lodash's _.groupBy() method can be used to group an array of objects based on a given property.

## Code explanation
**

1. `const people = [ { name: 'John', age: 20 }, { name: 'Jane', age: 30 }, { name: 'Jack', age: 20 }, { name: 'Jill', age: 30 } ];` - An array of objects representing people and containing their name and age.
2. `const groupedPeople = _.groupBy(people, 'age');` - Using Lodash's _.groupBy() method to group the array of objects by age.
3. `{ 20: [ { name: 'John', age: 20 }, { name: 'Jack', age: 20 } ], 30: [ { name: 'Jane', age: 30 }, { name: 'Jill', age: 30 } ] }` - The output of the _.groupBy() method, an object with two keys, one for each age, containing an array of objects representing the people with that age.

**## Helpful links**

- [Lodash Documentation - _.groupBy()](https://lodash.com/docs/4.17.15#groupBy)

onelinerhub: [How can I use Lodash to group an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-group-an-array-of-objects-in-javascript)