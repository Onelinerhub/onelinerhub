# How do I use Lodash to flatten an object in JavaScript?
// plain

Using Lodash, you can flatten an object in JavaScript by using the `_.flatten()` method. This method takes a single argument, which can be an array or an object.

For example:

```
const object = {
  a: {
    b: {
      c: 1
    },
    d: 2
  }
};

const flattened = _.flatten(object);

console.log(flattened);
```

## Output example


```
[ { c: 1 }, 2 ]
```

The `_.flatten()` method takes an object and returns a flattened array of the object's values. In the example above, the object `object` contains a nested object `a` with two values, `b` and `d`. After running the `_.flatten()` method, the output is an array containing these two values.

For more details on the `_.flatten()` method, see the [Lodash documentation](https://lodash.com/docs/4.17.15#flatten).

onelinerhub: [How do I use Lodash to flatten an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-flatten-an-object-in-javascript-1687009374)