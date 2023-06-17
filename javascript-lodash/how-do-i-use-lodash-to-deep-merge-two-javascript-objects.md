# How do I use Lodash to deep merge two JavaScript objects?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of the functions it provides is `_.merge()` which can be used to deep merge two JavaScript objects. The `_.merge()` function takes two objects as arguments and returns a new object that is the result of merging the two objects.

## Example code

```
const obj1 = {
  a: 1,
  b: 2,
  c: {
    d: 3,
    e: 4
  }
};

const obj2 = {
  b: 3,
  c: {
    f: 5
  }
};

const mergedObj = _.merge(obj1, obj2);

console.log(mergedObj);
```

## Output example

```
{
  a: 1,
  b: 3,
  c: {
    d: 3,
    e: 4,
    f: 5
  }
}
```

- `_.merge()`: function provided by Lodash to deep merge two JavaScript objects.
- `obj1`: first object to be merged.
- `obj2`: second object to be merged.
- `mergedObj`: new object created by merging `obj1` and `obj2`.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [GitHub Repository](https://github.com/lodash/lodash)

onelinerhub: [How do I use Lodash to deep merge two JavaScript objects?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-deep-merge-two-javascript-objects)