# How can I use Lodash to find and update an object in a JavaScript array?
// plain

Lodash is a JavaScript library that provides helpful utility functions for manipulating data. It can be used to find and update an object in a JavaScript array. The _.find() and _.assign() functions can be used together to accomplish this.

The _.find() function takes a collection (array, object, etc.) and a predicate (function) as arguments. It will iterate through the collection and return the first element that satisfies the predicate.

The _.assign() function is used to copy the values of all enumerable own properties from one or more source objects to a target object.

For example, given the following array of objects:

```
const array = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' }
]
```

We can use Lodash to find the object with an id of 2 and update its name to 'Charlie':

```
const updatedObject = _.assign(
  _.find(array, {id: 2}),
  {name: 'Charlie'}
);

console.log(updatedObject);
// { id: 2, name: 'Charlie' }
```

The _.find() function will return the object with an id of 2, and the _.assign() function will copy the new name value to the object, returning the updated object.

## Helpful links
* [Lodash Documentation](https://lodash.com/docs/)
* [_.find() Documentation](https://lodash.com/docs/4.17.15#find)
* [_.assign() Documentation](https://lodash.com/docs/4.17.15#assign)

onelinerhub: [How can I use Lodash to find and update an object in a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-and-update-an-object-in-a-javascript-array)