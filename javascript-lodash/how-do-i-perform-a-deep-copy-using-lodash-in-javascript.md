# How do I perform a deep copy using Lodash in JavaScript?
// plain

To perform a deep copy using Lodash in JavaScript, we can use the `_.cloneDeep()` method. This method will create a deep copy of the given value, meaning that the original and the copy will not share references.

## Example

```
const originalObj = {
    a: 1,
    b: {
        c: 2
    }
};

const deepCopy = _.cloneDeep(originalObj);

console.log(originalObj);
// { a: 1, b: { c: 2 } }

console.log(deepCopy);
// { a: 1, b: { c: 2 } }
```

In this example, we have an object `originalObj` that contains two properties, `a` and `b`. We then use the `_.cloneDeep()` method to create a deep copy of the object, assigned to the variable `deepCopy`. The output of the `console.log` statements reveals that both `originalObj` and `deepCopy` are the same, meaning that the deep copy was successful.

Parts of the code and explanation:
- `const originalObj = {...}`: this is the original object that we want to make a deep copy of.
- `const deepCopy = _.cloneDeep(originalObj)`: this is where we use the `_.cloneDeep()` method to create a deep copy of `originalObj`.
- `console.log(originalObj)`: this line logs the original object to the console.
- `console.log(deepCopy)`: this line logs the deep copy of the original object to the console.

## Helpful links
- [Lodash Documentation - cloneDeep](https://lodash.com/docs/4.17.15#cloneDeep)

onelinerhub: [How do I perform a deep copy using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-perform-a-deep-copy-using-lodash-in-javascript)