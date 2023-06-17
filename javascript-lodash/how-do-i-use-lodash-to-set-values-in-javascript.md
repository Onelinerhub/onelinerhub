# How do I use lodash to set values in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to set values in JavaScript in a few different ways.

1. Using the `_.set()` function:

```
let obj = {
  name: 'John'
};

_.set(obj, 'age', 24);

console.log(obj);
// { name: 'John', age: 24 }
```
The `_.set()` function takes two arguments: an object and a path, and sets the value of the path to the given value. In the example above, we set the `age` property of the `obj` object to `24`.

2. Using the `_.assign()` function:

```
let obj = {
  name: 'John'
};

_.assign(obj, { age: 24 });

console.log(obj);
// { name: 'John', age: 24 }
```
The `_.assign()` function takes two arguments: an object and a source object, and assigns the properties of the source object to the given object. In the example above, we assign the `age` property of the `obj` object to `24`.

3. Using the spread operator:

```
let obj = {
  name: 'John'
};

obj = { ...obj, age: 24 };

console.log(obj);
// { name: 'John', age: 24 }
```
The spread operator can be used to spread the properties of an object into another object. In the example above, we spread the properties of the `obj` object into a new object, and set the `age` property to `24`.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs)
- [MDN - Spread Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

onelinerhub: [How do I use lodash to set values in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-set-values-in-javascript)