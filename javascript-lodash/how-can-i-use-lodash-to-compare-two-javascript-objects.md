# How can I use Lodash to compare two JavaScript objects?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to compare two JavaScript objects.

One way to compare two objects is to use the _.isEqual() function. This function will take two objects as arguments and return true if they are equal, or false if they are not.

## Example


```
const object1 = {
  name: 'John',
  age: 20
};

const object2 = {
  name: 'John',
  age: 20
};

console.log(_.isEqual(object1, object2));
// Output: true
```

The _.isEqual() function will compare the values of each property in the two objects and return true if they are equal, or false if they are not. It will also check the types of the values, so that two objects with the same values but different types will not be considered equal.

Another way to compare two objects is to use the _.isMatch() function. This function takes two objects as arguments and returns true if the first object contains all the properties of the second object and the values of those properties are equal.

## Example


```
const object1 = {
  name: 'John',
  age: 20
};

const object2 = {
  name: 'John'
};

console.log(_.isMatch(object1, object2));
// Output: true
```

The _.isMatch() function will compare the first object to the second object and return true if all the properties of the second object are present in the first object and the values of those properties are equal.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [Lodash isEqual() Documentation](https://lodash.com/docs/4.17.15#isEqual)
- [Lodash isMatch() Documentation](https://lodash.com/docs/4.17.15#isMatch)

onelinerhub: [How can I use Lodash to compare two JavaScript objects?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-compare-two-javascript-objects)