# How can I use Lodash to let JavaScript do something?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to let JavaScript do something in a more efficient way.

For example, the `_.assign()` method can be used to copy the values of all enumerable own properties from one or more source objects to a target object.

```js
const source1 = { a: 1, b: 2 };
const source2 = { b: 4, c: 5 };

const target = { a: 0, b: 3, c: 6 };

_.assign(target, source1, source2);
// { a: 1, b: 4, c: 5 }
```

In the example above, the `_.assign()` method is used to copy the values of source1 and source2 to the target object. After the operation, the target object will contain the values of source1 and source2.

## Code explanation


- `_.assign()`: the Lodash method used to copy the values of source1 and source2 to the target object.
- `source1`: an object containing the values to be copied.
- `source2`: an object containing the values to be copied.
- `target`: the target object to which the values will be copied.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [_.assign() Documentation](https://lodash.com/docs/4.17.15#assign)

onelinerhub: [How can I use Lodash to let JavaScript do something?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-let-javascript-do-something)