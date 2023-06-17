# How do I use Lodash to deep clone an object in JavaScript?
// plain

Lodash is a JavaScript library that provides utilities for manipulating and iterating over objects and collections. It has a `_.cloneDeep()` method which can be used to deep clone an object.

```
const obj = {
  a: 1,
  b: {
    c: 2
  }
};

const clonedObj = _.cloneDeep(obj);

console.log(clonedObj);
// Output: { a: 1, b: { c: 2 } }
```

The `_.cloneDeep()` method takes a source object as an argument and returns a new object with all of its properties and values cloned from the source. It is a deep cloning operation, meaning that it will also clone any nested objects or collections.

The code above creates an `obj` object with a nested property `b`. It then uses the `_.cloneDeep()` method to create a new object, `clonedObj`, which is a clone of the original `obj` object.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [Lodash GitHub Repo](https://github.com/lodash/lodash)

onelinerhub: [How do I use Lodash to deep clone an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-deep-clone-an-object-in-javascript)