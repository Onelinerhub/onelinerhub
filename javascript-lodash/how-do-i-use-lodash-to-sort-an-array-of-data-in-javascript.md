# How do I use Lodash to sort an array of data in JavaScript?
// plain

Using Lodash to sort an array of data in JavaScript is easy. To do this, you can use the `_.sortBy()` method. This method takes two arguments: the array to be sorted and a function that defines the sorting criteria.

For example, to sort an array of objects by the `name` property in ascending order, you could use the following code:

```
const data = [
  { name: 'John', age: 32 },
  { name: 'Jane', age: 25 },
  { name: 'Adam', age: 28 }
]

const sortedData = _.sortBy(data, ['name'])

console.log(sortedData)
// Output: [{ name: 'Adam', age: 28 }, { name: 'Jane', age: 25 }, { name: 'John', age: 32 }]
```

The `_.sortBy()` method works by taking the array provided as the first argument and mapping each element to the value returned by the function provided as the second argument. It then sorts the mapped elements in ascending order.

You can also provide multiple sorting criteria, as well as specify the sorting order (ascending or descending).

Parts of code:
- `const data`: declaring a constant variable to hold the array of data
- `const sortedData = _.sortBy(data, ['name'])`: using the `_.sortBy()` method to sort the array of data by the `name` property in ascending order
- `console.log(sortedData)`: logging the sorted array to the console

## Helpful links
- [Lodash Documentation: `_.sortBy()`](https://lodash.com/docs/4.17.15#sortBy)

onelinerhub: [How do I use Lodash to sort an array of data in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-sort-an-array-of-data-in-javascript)