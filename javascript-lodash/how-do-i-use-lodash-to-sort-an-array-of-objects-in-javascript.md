# How do I use Lodash to sort an array of objects in JavaScript?
// plain

Using Lodash to sort an array of objects in JavaScript is a simple process. First, you must include the Lodash library in your code. Then you can use the _.sortBy() function to sort the array.

```
let array = [
    {name: 'John', age: 30},
    {name: 'Mary', age: 25},
    {name: 'Bob', age: 27},
];

let sortedArray = _.sortBy(array, 'age');

console.log(sortedArray);
```

## Output example

```
[
    {name: 'Mary', age: 25},
    {name: 'Bob', age: 27},
    {name: 'John', age: 30},
]
```

The code above uses the _.sortBy() function to sort the array of objects by the age property. The _.sortBy() function takes two arguments: the array to be sorted and the property to sort by. It returns a new array sorted in ascending order.

Parts of the code:
* `let array`: Defines an array of objects to be sorted.
* `let sortedArray = _.sortBy(array, 'age')`: Sorts the array of objects by the age property using the Lodash _.sortBy() function.
* `console.log(sortedArray)`: Logs the sorted array of objects to the console.

## Helpful links
* [Lodash Documentation - _.sortBy()](https://lodash.com/docs/4.17.15#sortBy)

onelinerhub: [How do I use Lodash to sort an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-sort-an-array-of-objects-in-javascript)