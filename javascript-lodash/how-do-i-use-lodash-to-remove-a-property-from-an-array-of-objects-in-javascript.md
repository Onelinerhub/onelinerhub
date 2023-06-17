# How do I use Lodash to remove a property from an array of objects in JavaScript?
// plain

Using Lodash, you can remove a property from an array of objects in JavaScript with the _.omit() method. This method takes two parameters: the array of objects and the key of the property to be removed.

## Example


```
const array = [
  { name: 'John', age: 30 },
  { name: 'Jane', age: 25 }
];

const newArray = _.omit(array, 'age');

console.log(newArray);
```
## Output example

```
[
  { name: 'John' },
  { name: 'Jane' }
]
```

The code above uses the Lodash _.omit() method to remove the `age` property from the `array` of objects. The output is a new array of objects with the `age` property removed.

## Code explanation

- `const array`: creates a variable to store the array of objects
- `_.omit(array, 'age')`: uses the Lodash _.omit() method to remove the `age` property from the `array` of objects
- `console.log(newArray)`: logs the new array of objects with the `age` property removed to the console

## Helpful links
- [Lodash Documentation - _.omit()](https://lodash.com/docs/#omit)

onelinerhub: [How do I use Lodash to remove a property from an array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-a-property-from-an-array-of-objects-in-javascript)