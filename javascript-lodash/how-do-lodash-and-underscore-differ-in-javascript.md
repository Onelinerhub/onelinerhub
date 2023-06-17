# How do lodash and underscore differ in JavaScript?
// plain

Lodash and Underscore are both JavaScript libraries that provide utility functions for common programming tasks. They are often used for manipulating and iterating over objects and collections.

The main difference between Lodash and Underscore is that Lodash was written to provide more modern JavaScript language features while Underscore was written to provide compatibility with older browsers.

For example, Lodash includes functions for working with Promises, Maps, and Sets, which are not available in Underscore.

Here is an example of how Lodash's `map()` function can be used to iterate over an array and return a new array with each element doubled:

```javascript
const arr = [1, 2, 3];
const doubledArray = _.map(arr, num => num * 2);
console.log(doubledArray);
```

## Output example

```
[2, 4, 6]
```

The `map()` function in Lodash is similar to the `map()` function in Underscore, but it has some additional features, such as the ability to pass in an object as the first argument instead of an array, and the ability to pass in a context object as the second argument.

Other differences between Lodash and Underscore include:

- Lodash has a larger and more active community, with more contributors and more frequent releases.
- Lodash is more modular, allowing you to import only the functions you need.
- Lodash is faster, with more optimized algorithms and fewer iterations.

## Helpful links
- [Lodash](https://lodash.com/)
- [Underscore](http://underscorejs.org/)

onelinerhub: [How do lodash and underscore differ in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-lodash-and-underscore-differ-in-javascript)