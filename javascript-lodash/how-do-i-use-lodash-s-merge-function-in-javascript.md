# How do I use lodash's merge function in JavaScript?
// plain

Lodash's `merge` function is used to combine two or more objects together into a single object. It takes in two or more objects and returns a new object with the properties from all of the objects combined.

## Example code

```
const obj1 = {
  prop1: 'value1',
  prop2: 'value2'
};
const obj2 = {
  prop3: 'value3',
  prop4: 'value4'
};

const mergedObj = _.merge(obj1, obj2);

console.log(mergedObj);
```

## Output example

```
{
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3',
  prop4: 'value4'
}
```

The code above creates two objects, `obj1` and `obj2`, and then uses lodash's `merge` function to combine them into a single object, `mergedObj`. The `mergedObj` now contains all the properties from both `obj1` and `obj2`.

Parts of the code:
- `const obj1 = {...}`: Creates an object with two properties, `prop1` and `prop2`.
- `const obj2 = {...}`: Creates an object with two properties, `prop3` and `prop4`.
- `const mergedObj = _.merge(obj1, obj2)`: Calls lodash's `merge` function to combine `obj1` and `obj2` into a single object, `mergedObj`.
- `console.log(mergedObj)`: Logs the `mergedObj` object to the console.

## Helpful links
- [Lodash Documentation - merge](https://lodash.com/docs/4.17.15#merge)

onelinerhub: [How do I use lodash's merge function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-merge-function-in-javascript)