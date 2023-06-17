# How do I use Lodash to group elements in an array by a given property in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to group elements in an array by a given property. To do this, we can use the `_.groupBy()` function. This function takes two arguments: an array and a callback function. The callback function should return the property by which we want to group the elements.

For example, let's say we have an array of objects that represent people, and each object has a `name` and an `age` property. We can use `_.groupBy()` to group the elements by age:

```javascript
const people = [
  { name: 'John', age: 20 },
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 20 },
];

const groupedPeople = _.groupBy(people, person => person.age);
```

The output of the code above will be:

```javascript
{
  20: [
    { name: 'John', age: 20 },
    { name: 'Bob', age: 20 },
  ],
  30: [
    { name: 'Alice', age: 30 },
  ],
}
```

- `people`: an array of objects that represent people, with `name` and `age` properties
- `groupedPeople`: the result of calling `_.groupBy()` on `people`, with the callback function returning the `age` property
- `_.groupBy()`: the Lodash function that takes an array and a callback function as arguments, and returns an object of grouped elements

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [MDN _.groupBy() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/groupBy)

onelinerhub: [How do I use Lodash to group elements in an array by a given property in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-group-elements-in-an-array-by-a-given-property-in-javascript)