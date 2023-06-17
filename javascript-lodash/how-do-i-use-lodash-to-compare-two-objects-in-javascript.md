# How do I use Lodash to compare two objects in JavaScript?
// plain

The Lodash library provides a `_.isEqual` function that can be used to compare two objects in JavaScript. This function takes two objects as arguments and returns `true` if they are equal, otherwise it returns `false`.

## Example code

```
const obj1 = {
  a: 1,
  b: 2,
  c: 3
};

const obj2 = {
  a: 1,
  b: 2,
  c: 3
};

console.log(_.isEqual(obj1, obj2));
```

## Output example

```
true
```

The code above uses Lodash to compare two objects `obj1` and `obj2`. The `_.isEqual` function is used to compare the two objects and it returns `true` if they are equal, otherwise it returns `false`.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [_.isEqual()](https://lodash.com/docs/4.17.15#isEqual)

onelinerhub: [How do I use Lodash to compare two objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-compare-two-objects-in-javascript)