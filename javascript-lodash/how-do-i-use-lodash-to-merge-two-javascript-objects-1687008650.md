# How do I use Lodash to merge two JavaScript objects?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of these tasks is merging two JavaScript objects. To do this, you can use the `_.merge()` function. This function takes two objects as arguments and returns a new object that contains the combined properties of both.

For example:
```
const obj1 = {
  a: 1,
  b: 2
};

const obj2 = {
  c: 3,
  d: 4
};

const mergedObj = _.merge(obj1, obj2);

console.log(mergedObj);
```

## Output example

```
{
  a: 1,
  b: 2,
  c: 3,
  d: 4
}
```

The `_.merge()` function can also take a third argument, which is an object containing options for customizing the merging process. This argument is optional.

## Code explanation


1. `const obj1 = { a: 1, b: 2 };` - This is the first object to be merged.
2. `const obj2 = { c: 3, d: 4 };` - This is the second object to be merged.
3. `const mergedObj = _.merge(obj1, obj2);` - This uses the `_.merge()` function to combine the two objects.
4. `console.log(mergedObj);` - This logs the result of the merging process.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [_.merge() Documentation](https://lodash.com/docs/4.17.15#merge)

onelinerhub: [How do I use Lodash to merge two JavaScript objects?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-merge-two-javascript-objects-1687008650)