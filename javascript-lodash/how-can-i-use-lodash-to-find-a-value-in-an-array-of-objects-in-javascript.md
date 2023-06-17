# How can I use Lodash to find a value in an array of objects in JavaScript?
// plain

Using Lodash, you can find a value in an array of objects in JavaScript by using the `_.find` method. This method will search for a given value in an array of objects and return the first element that matches the given criteria.

For example, given the following array of objects:

```
const arr = [
  {
    name: 'John',
    age: 32
  },
  {
    name: 'Mary',
    age: 25
  },
  {
    name: 'Jane',
    age: 28
  }
]
```

You can use Lodash's `_.find` method to search for an object with the name 'John' like so:

```
const john = _.find(arr, {name: 'John'});

console.log(john);
// Output: { name: 'John', age: 32 }
```

The `_.find` method takes two arguments, the first being the array to search and the second being an object with the criteria to search for. In this example, we are searching for an object with the name 'John'.

The `_.find` method will return the first element that matches the given criteria, in this case it will return the object `{name: 'John', age: 32}`.

For more information, you can refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#find).

onelinerhub: [How can I use Lodash to find a value in an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-a-value-in-an-array-of-objects-in-javascript)