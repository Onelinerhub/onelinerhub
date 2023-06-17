# How do I use Lodash to group an array in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to group an array in JavaScript with the _.groupBy() method.

## Example


```
const array = [
  {name: 'John', age: 20},
  {name: 'Jane', age: 20},
  {name: 'Bob', age: 21},
  {name: 'Alice', age: 21}
];

const groupedArray = _.groupBy(array, 'age');

console.log(groupedArray);
```

## Output example

```
{
  20: [
    {name: 'John', age: 20},
    {name: 'Jane', age: 20}
  ],
  21: [
    {name: 'Bob', age: 21},
    {name: 'Alice', age: 21}
  ]
}
```

The code above uses Lodash's _.groupBy() method to group the array of objects by age. The _.groupBy() method takes two arguments: an array of values and a key to group by. It returns an object with the keys being the grouped values and the values being an array of objects with that key.

## Code explanation


1. `const array = [...];` - declares an array of objects to be grouped.
2. `const groupedArray = _.groupBy(array, 'age');` - uses the _.groupBy() method to group the array by age.
3. `console.log(groupedArray);` - logs the grouped array to the console.

## Helpful links

- [Lodash documentation](https://lodash.com/docs/)
- [_.groupBy() method documentation](https://lodash.com/docs/4.17.15#groupBy)

onelinerhub: [How do I use Lodash to group an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-group-an-array-in-javascript)