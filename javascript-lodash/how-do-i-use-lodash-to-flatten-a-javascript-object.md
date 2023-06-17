# How do I use Lodash to flatten a JavaScript object?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of the functions it provides is `_.flatten`, which can be used to flatten a JavaScript object.

To use `_.flatten`, pass in the object that you want to flatten as the first argument. The second argument is an optional boolean value which, if true, will also flatten arrays within the object.

```js
const obj = {
  a: 1,
  b: {
    c: 2,
    d: 3
  },
  e: [4, 5, 6]
};

const flattenedObj = _.flatten(obj);
console.log(flattenedObj);
```

## Output example

```
[1, 2, 3, 4, 5, 6]
```

The code above uses `_.flatten` to flatten the object `obj`. The output is an array containing all the values from the object, in the order they were found.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [_.flatten](https://lodash.com/docs/4.17.15#flatten)

onelinerhub: [How do I use Lodash to flatten a JavaScript object?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-flatten-a-javascript-object)