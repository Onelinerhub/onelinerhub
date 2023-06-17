# How can I use Lodash to merge objects with the same key in JavaScript?
// plain

Using Lodash, you can easily merge objects with the same key in JavaScript. To do this, you can use the `_.merge()` method. This method takes two objects as arguments and merges them together. The resulting object will contain all the properties from both objects, with the properties from the second object overriding the ones from the first.

For example, the following code:
```
const obj1 = {
    a: 1,
    b: 2
};

const obj2 = {
    a: 3,
    c: 4
};

const merged = _.merge(obj1, obj2);

console.log(merged);
```

will output:
```
{
    a: 3,
    b: 2,
    c: 4
}
```

The code works as follows:
1. We define two objects, `obj1` and `obj2`, with the same key `a` but different values.
2. We use Lodash's `_.merge()` method to merge the two objects together.
3. The resulting object, `merged`, contains all the properties from both objects, with the properties from the second object overriding the ones from the first.

For more information on Lodash's `_.merge()` method, see [the Lodash documentation](https://lodash.com/docs/4.17.15#merge).

onelinerhub: [How can I use Lodash to merge objects with the same key in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-merge-objects-with-the-same-key-in-javascript)