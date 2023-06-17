# How do I use Lodash to merge two objects in JavaScript?
// plain

Using Lodash to merge two objects in JavaScript is very easy. All you need to do is call the `_.merge()` method, passing in the two objects as arguments.

```
let obj1 = {
  name: 'John',
  age: 30
};

let obj2 = {
  name: 'Jane',
  city: 'New York'
};

let mergedObj = _.merge(obj1, obj2);

console.log(mergedObj);
```

## Output example

```
{
  name: 'Jane',
  age: 30,
  city: 'New York'
}
```

The `_.merge()` method will merge the two objects, overriding any duplicate keys with the values from the second object. In this example, the `name` key was overridden with the value from `obj2`.

It's also possible to pass in a third argument to the `_.merge()` method, which is a customizer function. This customizer function allows you to customize the merging process, and can be used to control how the two objects are merged.

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15#merge).

onelinerhub: [How do I use Lodash to merge two objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-merge-two-objects-in-javascript)