# How do I sort an array of objects in JavaScript using Lodash?
// plain

Using Lodash, you can sort an array of objects in JavaScript by using the `_.sortBy()` method. This method takes in an array of objects and a property name as arguments and returns a sorted array based on the property name.

For example, given an array of objects like this:

```
const arr = [
    {name: 'John', age: 25},
    {name: 'Jane', age: 30},
    {name: 'Adam', age: 20}
];
```

You can sort it by age using the `_.sortBy()` method like this:

```
const sortedArr = _.sortBy(arr, 'age');

console.log(sortedArr);

// Output:
// [
//   { name: 'Adam', age: 20 },
//   { name: 'John', age: 25 },
//   { name: 'Jane', age: 30 }
// ]
```

The `_.sortBy()` method works by looping through each item in the array and comparing the property values. It then uses the comparison result to determine the order of the items in the returned array.

Here's a breakdown of the code:

1. `const sortedArr = _.sortBy(arr, 'age')`: This declares a new variable `sortedArr` and assigns the result of the `_.sortBy()` method to it. The `_.sortBy()` method takes two arguments: an array and a property name.

2. `console.log(sortedArr)`: This logs the sorted array to the console.

## Helpful links

- [Lodash Documentation - _.sortBy()](https://lodash.com/docs/4.17.15#sortBy)

onelinerhub: [How do I sort an array of objects in JavaScript using Lodash?](https://onelinerhub.com/javascript-lodash/how-do-i-sort-an-array-of-objects-in-javascript-using-lodash)