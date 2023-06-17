# How can I use Lodash to get a value from an array of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of its many features is the ability to easily get a value from an array of objects. Here's an example of how to do this:

```
// example array of objects
const arrayOfObjects = [
  {name: 'John', age: 30},
  {name: 'Jane', age: 20},
  {name: 'Jack', age: 25}
];

// use Lodash to get the value of the 'age' property from the second object
const age = _.get(arrayOfObjects, '[1].age');

console.log(age);
// Output: 20
```

The code above uses the Lodash `_.get()` function to get the value of the `age` property from the second object in the `arrayOfObjects`. The first argument is the array of objects, and the second argument is a string that specifies the path to the value we want to get. In this case, `[1].age` means the `age` property of the second object in the array.

## Code explanation


1. `const arrayOfObjects = [ {name: 'John', age: 30}, {name: 'Jane', age: 20}, {name: 'Jack', age: 25} ];` - This declares a constant called `arrayOfObjects` and assigns it an array of objects.

2. `const age = _.get(arrayOfObjects, '[1].age');` - This uses the Lodash `_.get()` function to get the value of the `age` property from the second object in the `arrayOfObjects` array. The first argument is the array of objects, and the second argument is a string that specifies the path to the value we want to get.

3. `console.log(age);` - This prints the value of the `age` variable to the console.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [MDN _.get() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/get)

onelinerhub: [How can I use Lodash to get a value from an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-get-a-value-from-an-array-of-objects-in-javascript)