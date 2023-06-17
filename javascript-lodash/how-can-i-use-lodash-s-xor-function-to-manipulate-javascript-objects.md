# How can I use Lodash's xor function to manipulate JavaScript objects?
// plain

Lodash's `xor` function can be used to manipulate JavaScript objects by performing a symmetric difference between two objects. This means that it will return properties that exist in one object but not in the other.

For example:

```
const a = {
  name: 'John',
  age: 30
};

const b = {
  name: 'John',
  address: 'London'
};

const result = _.xor(a, b);

console.log(result);
```

## Output example

```
[ { age: 30 }, { address: 'London' } ]
```

The `xor` function will return an array of objects, with the properties that exist in one object but not in the other. In this case, `age` exists in `a` but not in `b`, and `address` exists in `b` but not in `a`.

The `xor` function can also be used to detect differences between two objects with the same properties. For example:

```
const a = {
  name: 'John',
  age: 30
};

const b = {
  name: 'John',
  age: 40
};

const result = _.xor(a, b);

console.log(result);
```

## Output example

```
[ { age: 30 }, { age: 40 } ]
```

In this case, the `xor` function will return an array of objects, with the properties that differ between the two objects. In this case, `age` is different in both objects.

The `xor` function can be used in a variety of ways to manipulate JavaScript objects.

## Helpful links
- [Lodash xor](https://lodash.com/docs/4.17.15#xor)
- [Symmetric Difference](https://en.wikipedia.org/wiki/Symmetric_difference)

onelinerhub: [How can I use Lodash's xor function to manipulate JavaScript objects?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-xor-function-to-manipulate-javascript-objects)