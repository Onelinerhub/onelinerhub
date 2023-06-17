# How do I use Lodash to sort an array of objects by a specific property in JavaScript?
// plain

To use Lodash to sort an array of objects by a specific property in JavaScript, you can use the `_.sortBy()` function. This function will take an array of objects and a property name as arguments and will return a new array sorted by the specified property.

For example:
```
const array = [
 { name: 'John', age: 30 },
 { name: 'Alice', age: 20 },
 { name: 'Bob', age: 25 }
];

const sortedArray = _.sortBy(array, 'age');

console.log(sortedArray);
```

## Output example

```
[
 { name: 'Alice', age: 20 },
 { name: 'Bob', age: 25 },
 { name: 'John', age: 30 }
]
```

- `const array`: declaring a constant variable and assigning it to an array of objects.
- `const sortedArray`: declaring a constant variable and assigning it to the result of calling `_.sortBy()` with the `array` variable and the property name `'age'` as arguments.
- `_.sortBy()`: Lodash function used to sort an array of objects by a specific property.

## Helpful links
- [Lodash Documentation - _.sortBy()](https://lodash.com/docs/4.17.15#sortBy)

onelinerhub: [How do I use Lodash to sort an array of objects by a specific property in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-sort-an-array-of-objects-by-a-specific-property-in-javascript)