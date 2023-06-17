# How can I use Lodash to compare two objects in JavaScript?
// plain

Lodash can be used to compare two objects in JavaScript by using the `_.isEqual()` function. This function will check if two objects have the same values.

For example:

```
const object1 = {
  name: 'John',
  age: 25
};

const object2 = {
  name: 'John',
  age: 25
};

console.log(_.isEqual(object1, object2));
```

## Output example
 `true`

The code above is using the `_.isEqual()` function to compare two objects and it will return true if the two objects have the same values.

The parts of the code are:

- `const object1 = {name: 'John', age: 25};`: This is creating an object with the name and age of a person.

- `const object2 = {name: 'John', age: 25};`: This is creating a second object with the same name and age of the first object.

- `console.log(_.isEqual(object1, object2));`: This is using the `_.isEqual()` function to compare the two objects and it will return `true` if they have the same values.

## Helpful links

- [Lodash Documentation - isEqual](https://lodash.com/docs/4.17.15#isEqual)

onelinerhub: [How can I use Lodash to compare two objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-compare-two-objects-in-javascript)