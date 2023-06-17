# How do I use Lodash's cloneDeep() method in JavaScript?
// plain

Lodash's `cloneDeep()` method is a powerful utility that can be used to create a deep clone of a given object. This can be useful when working with objects that contain nested properties.

## Example code

```javascript
const _ = require('lodash');

const originalObject = {
  name: 'John',
  age: 30,
  address: {
    city: 'London',
    country: 'UK'
  }
}

const clonedObject = _.cloneDeep(originalObject);

console.log(clonedObject);
```

## Output example

```
{
  name: 'John',
  age: 30,
  address: { city: 'London', country: 'UK' }
}
```

The code above will create a deep clone of the original object, meaning that the new object (`clonedObject`) will contain the same properties and values as the original object (`originalObject`).

The `cloneDeep()` method can also be used to clone arrays, functions, and other complex data types.

## Code explanation

* `require('lodash')` - imports the lodash library
* `_.cloneDeep(originalObject)` - creates a deep clone of the original object
* `console.log(clonedObject)` - prints the cloned object to the console

## Helpful links
* [Lodash Documentation](https://lodash.com/docs/4.17.15)
* [MDN: Object.assign()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

onelinerhub: [How do I use Lodash's cloneDeep() method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-clonedeep---method-in-javascript)