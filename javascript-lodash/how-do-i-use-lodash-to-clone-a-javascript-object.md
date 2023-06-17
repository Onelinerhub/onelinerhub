# How do I use Lodash to clone a JavaScript object?
// plain

Using Lodash to clone a JavaScript object is a quick and easy way to create a copy of an existing object. The `_.cloneDeep()` method can be used to clone an object and all of its nested properties.

## Example

```
const originalObject = {
  name: 'John',
  age: 30,
  address: {
    street: '123 Main Street',
    city: 'New York',
    state: 'NY'
  }
};

const clonedObject = _.cloneDeep(originalObject);

console.log(clonedObject);
```
## Output example

```
{
  name: 'John',
  age: 30,
  address: {
    street: '123 Main Street',
    city: 'New York',
    state: 'NY'
  }
}
```

The code above uses the Lodash `_.cloneDeep()` method to create a clone of the original object. It takes the original object as an argument and returns a deep copy of the object. The cloned object will have the same properties and values as the original object.

## Code explanation

1. `const originalObject = {...}`: This creates an object literal that will be used as the original object to be cloned.
2. `const clonedObject = _.cloneDeep(originalObject)`: This uses the Lodash `_.cloneDeep()` method to clone the original object.
3. `console.log(clonedObject)`: This logs the cloned object to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [Lodash `_.cloneDeep()` Documentation](https://lodash.com/docs/4.17.15#cloneDeep)

onelinerhub: [How do I use Lodash to clone a JavaScript object?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-clone-a-javascript-object)