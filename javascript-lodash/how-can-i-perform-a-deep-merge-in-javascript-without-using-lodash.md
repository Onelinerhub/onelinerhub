# How can I perform a deep merge in JavaScript without using Lodash?
// plain

A deep merge in JavaScript can be performed without using Lodash by using a recursive function to iterate through the objects and properties. The following example code block will merge two objects into one, and overwrite any properties with the same name:

```
let obj1 = {
  a: 1,
  b: 2,
  c: {
    d: 3
  }
}

let obj2 = {
  a: 4,
  b: 5,
  c: {
    e: 6
  }
}

function deepMerge(obj1, obj2) {
  let result = {...obj1, ...obj2};
  for (let key in result) {
    if (typeof result[key] === 'object') {
      result[key] = deepMerge(obj1[key], obj2[key]);
    }
  }
  return result;
}

console.log(deepMerge(obj1, obj2));
```

## Output example

```
{
  a: 4,
  b: 5,
  c: {
    d: 3,
    e: 6
  }
}
```

## Code explanation

1. The `let result = {...obj1, ...obj2};` line creates a new object with the properties of both `obj1` and `obj2`.
2. The `for (let key in result) {` loop iterates through the properties of the `result` object.
3. The `if (typeof result[key] === 'object') {` condition checks if the property is an object.
4. The `result[key] = deepMerge(obj1[key], obj2[key]);` line passes the corresponding properties of `obj1` and `obj2` to the `deepMerge()` function and assigns the returned value to the `result` object.

## Helpful links
- [MDN - Object.assign()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
- [MDN - Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

onelinerhub: [How can I perform a deep merge in JavaScript without using Lodash?](https://onelinerhub.com/javascript-lodash/how-can-i-perform-a-deep-merge-in-javascript-without-using-lodash)