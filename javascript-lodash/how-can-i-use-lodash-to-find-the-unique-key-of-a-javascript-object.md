# How can I use Lodash to find the unique key of a JavaScript object?
// plain

Lodash provides a useful method for finding the unique keys of a JavaScript object: `_.keys()`. This method takes an object as an argument and returns an array of the object's keys.

For example:

```
const object = {
  a: 1,
  b: 2,
  c: 3
};

const uniqueKeys = _.keys(object);

console.log(uniqueKeys);
```

## Output example

```
[a, b, c]
```

The `_.keys()` method:

- takes an object as an argument
- returns an array of the object's keys

## Helpful links

- [Lodash Documentation - _.keys()](https://lodash.com/docs/4.17.15#keys)

onelinerhub: [How can I use Lodash to find the unique key of a JavaScript object?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-the-unique-key-of-a-javascript-object)