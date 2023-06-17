# How do I use Lodash to merge two objects in JavaScript?
// plain

Using Lodash to merge two objects in JavaScript is simple and straightforward. The `_.merge()` method can be used to combine two objects into one.

For example:
```
let obj1 = {
  a: 1,
  b: 2
};

let obj2 = {
  c: 3,
  d: 4
};

let obj3 = _.merge(obj1, obj2);

console.log(obj3);
```

## Output example

```
{
  a: 1,
  b: 2,
  c: 3,
  d: 4
}
```

The code above uses the `_.merge()` method to combine two objects, `obj1` and `obj2`, into one object, `obj3`. The `_.merge()` method takes two parameters – the two objects to be merged – and returns a new object with the combined properties.

In the example above, the result is an object with the properties from both `obj1` and `obj2`.

### List of Code Parts

1. `let obj1 = { a: 1, b: 2 };` - creates a new object with two properties, `a` and `b`.
2. `let obj2 = { c: 3, d: 4 };` - creates a new object with two properties, `c` and `d`.
3. `let obj3 = _.merge(obj1, obj2);` - uses the `_.merge()` method to combine the two objects, `obj1` and `obj2`, into one object, `obj3`.
4. `console.log(obj3);` - logs the combined object, `obj3`, to the console.

### Relevant Links

- [Lodash Documentation - _.merge()](https://lodash.com/docs/4.17.15#merge)

onelinerhub: [How do I use Lodash to merge two objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-merge-two-objects-in-javascript-1687009745)