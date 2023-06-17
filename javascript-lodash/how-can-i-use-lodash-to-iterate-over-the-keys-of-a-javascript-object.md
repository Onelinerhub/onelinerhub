# How can I use Lodash to iterate over the keys of a JavaScript object?
// plain

Using Lodash you can iterate over the keys of a JavaScript object by using the `_.keys()` function. This will return an array of the object's keys.

## Example

```
const object = {
  name: 'John Doe',
  age: 25
}

const keys = _.keys(object);
console.log(keys);
```
## Output example

```
[ 'name', 'age' ]
```

The `_.keys()` function takes in an object as an argument and returns an array of the object's keys. The array will contain the key names as strings.

You can then use the Lodash `_.each()` function to iterate over the array of keys and perform some action on each key.

## Example

```
_.each(keys, (key) => {
  console.log(key);
});
```
## Output example

```
name
age
```

The `_.each()` function takes in an array and a callback function as arguments. The callback function will be called for each element in the array and will be passed the current element as an argument. In this case, the current element is the key name.

## Helpful links
- [Lodash _.keys()](https://lodash.com/docs/4.17.15#keys)
- [Lodash _.each()](https://lodash.com/docs/4.17.15#each)

onelinerhub: [How can I use Lodash to iterate over the keys of a JavaScript object?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-iterate-over-the-keys-of-a-javascript-object)