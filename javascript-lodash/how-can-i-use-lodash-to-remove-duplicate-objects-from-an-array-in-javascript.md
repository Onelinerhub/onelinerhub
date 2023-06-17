# How can I use Lodash to remove duplicate objects from an array in JavaScript?
// plain

Lodash provides a convenient method for removing duplicate objects from an array in JavaScript, `_.uniqWith()`. This method takes two arguments: an array of objects, and a comparison function. The comparison function should return `true` if two objects are considered equal, and `false` otherwise.

For example, given an array of objects, `arr`, we can use `_.uniqWith()` to remove duplicates as follows:

```
const arr = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Bob' },
  { id: 1, name: 'John' }
];

const dedupedArray = _.uniqWith(arr, (a, b) => a.id === b.id);

console.log(dedupedArray);
```

## Output example

```
[
  { id: 1, name: 'John' },
  { id: 2, name: 'Bob' }
]
```

The above code uses `_.uniqWith()` to compare objects based on their `id` property. It returns a new array with the duplicate objects removed.

Parts of the code and explanation:

- `const arr = [ ... ]`: This declares an array of objects.
- `_.uniqWith(arr, (a, b) => a.id === b.id)`: This is the call to `_.uniqWith()`, which takes two arguments: the array of objects, and a comparison function. The comparison function should return `true` if two objects are considered equal, and `false` otherwise. In this case, the comparison function compares the `id` property of two objects and returns `true` if they are equal.
- `console.log(dedupedArray)`: This logs the result of the `_.uniqWith()` call to the console.

## Helpful links

- [Lodash documentation for `_.uniqWith()`](https://lodash.com/docs/4.17.15#uniqWith)

onelinerhub: [How can I use Lodash to remove duplicate objects from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-duplicate-objects-from-an-array-in-javascript)