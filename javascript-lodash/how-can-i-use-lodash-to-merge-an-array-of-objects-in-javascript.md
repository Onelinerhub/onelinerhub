# How can I use Lodash to merge an array of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for manipulating objects and collections. One of its utility functions is `_.merge()`, which can be used to merge an array of objects in JavaScript.

The `_.merge()` function takes two parameters: the target object and the source object. It will merge the source object into the target object, and return the target object.

## Example


```javascript
const target = { a: 1 };
const source = [{ b: 2 }, { c: 3 }];

console.log(_.merge(target, source));
// Output: { a: 1, b: 2, c: 3 }
```

In this example, the `_.merge()` function merges the source array of objects into the target object, resulting in an object that contains the properties of both the target and source objects.

The `_.merge()` function can also be used to deep merge objects, which means that it will merge the properties of nested objects as well.

## Example


```javascript
const target = { a: { b: 1 } };
const source = { a: { c: 2 } };

console.log(_.merge(target, source));
// Output: { a: { b: 1, c: 2 } }
```

In this example, the `_.merge()` function merges the properties of the source object into the target object, resulting in an object that contains the properties of both the target and source objects, including the nested objects.

## Helpful links
* [Lodash Documentation](https://lodash.com/docs/)
* [_.merge() Documentation](https://lodash.com/docs/4.17.15#merge)

onelinerhub: [How can I use Lodash to merge an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-merge-an-array-of-objects-in-javascript)