# How can I use Lodash to sort an array of objects by key value in JavaScript?
// plain

Using Lodash, you can sort an array of objects by key value in JavaScript by using the `_.sortBy()` method. This method takes an array and a sorting function as its arguments. The sorting function should take an object as its argument and return the value to sort by.

For example:
```
let arr = [
  { name: 'John', age: 20 },
  { name: 'Jane', age: 18 },
  { name: 'Bob', age: 22 }
];

let sorted = _.sortBy(arr, o => o.age);

console.log(sorted);
```

## Output example

```
[
  { name: 'Jane', age: 18 },
  { name: 'John', age: 20 },
  { name: 'Bob', age: 22 }
]
```

The `_.sortBy()` method takes an array, `arr`, and a sorting function as its arguments. The sorting function, `o => o.age`, takes an object, `o`, as its argument and returns the value to sort by, `o.age`. The sorted array is then stored in the `sorted` variable. The output of the code is an array of objects sorted by age.

## Helpful links
- [Lodash Documentation - _.sortBy()](https://lodash.com/docs/4.17.15#sortBy)

onelinerhub: [How can I use Lodash to sort an array of objects by key value in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-sort-an-array-of-objects-by-key-value-in-javascript)