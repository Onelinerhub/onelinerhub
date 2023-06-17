# How can I use Lodash to change the key name of an object in JavaScript?
// plain

Using Lodash, you can easily change the key name of an object in JavaScript. Lodash provides a `_.mapKeys()` function that can be used to map the keys of an object to a new set of keys.

For example, given the following object:

```
const obj = {
    name: 'John',
    age: 25
};
```

You can use `_.mapKeys()` to change the key names to `firstName` and `yearsOld` like this:

```
const newObj = _.mapKeys(obj, (value, key) => {
    return key === 'name' ? 'firstName' : 'yearsOld';
});

console.log(newObj);
// Output: { firstName: 'John', yearsOld: 25 }
```

The `_.mapKeys()` function takes two arguments: the object to map and a function that determines the mapping of each key. In the example above, the function returns `firstName` if the key is `name`, and `yearsOld` otherwise.

## Code explanation


- `const obj = { name: 'John', age: 25 };`: This creates an object with two keys, `name` and `age`.
- `const newObj = _.mapKeys(obj, (value, key) => { ... });`: This uses Lodash's `_.mapKeys()` function to map the keys of the object to a new set of keys.
- `return key === 'name' ? 'firstName' : 'yearsOld';`: This is the function that determines the mapping of each key. It returns `firstName` if the key is `name`, and `yearsOld` otherwise.

Here are some relevant links if you need more information:

- [Lodash Documentation: _.mapKeys()](https://lodash.com/docs/4.17.15#mapKeys)
- [MDN: Object.keys()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)

onelinerhub: [How can I use Lodash to change the key name of an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-change-the-key-name-of-an-object-in-javascript)