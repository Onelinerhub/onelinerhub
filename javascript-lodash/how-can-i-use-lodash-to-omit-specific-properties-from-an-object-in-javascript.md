# How can I use Lodash to omit specific properties from an object in Javascript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to omit specific properties from an object in JavaScript using the _.omit() function.

## Example code

```
const object = {
    name: 'John',
    age: 25,
    job: 'engineer'
};

const omittedObject = _.omit(object, ['age']);

console.log(omittedObject);
```
## Output example

```
{ name: 'John', job: 'engineer' }
```

The code above uses the _.omit() function to omit the 'age' property from the object. The first argument of the function is the object, and the second argument is an array of the properties to omit. The function returns a new object with the omitted properties.

Parts of the code:

1. `const object = {...};`: This creates an object with three properties.
2. `const omittedObject = _.omit(object, ['age']);`: This uses the _.omit() function to omit the 'age' property from the object.
3. `console.log(omittedObject);`: This logs the new object with the omitted property to the console.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [_.omit() Documentation](https://lodash.com/docs/4.17.15#omit)

onelinerhub: [How can I use Lodash to omit specific properties from an object in Javascript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-omit-specific-properties-from-an-object-in-javascript)