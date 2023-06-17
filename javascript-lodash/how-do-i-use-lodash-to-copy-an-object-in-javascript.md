# How do I use Lodash to copy an object in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to easily copy an object in JavaScript.

## Example

```
const _ = require('lodash');

const obj1 = {
  name: 'John',
  age: 30
};

const obj2 = _.cloneDeep(obj1);

console.log(obj2);
```
## Output example

```
{
  name: 'John',
  age: 30
}
```

The code above uses the Lodash `cloneDeep` method to copy an object. This method creates a deep clone of the object, meaning that any nested objects will also be cloned.

The code can be broken down as follows:

1. `const _ = require('lodash');` - imports the Lodash library.
2. `const obj1 = {name: 'John', age: 30};` - creates an object to be cloned.
3. `const obj2 = _.cloneDeep(obj1);` - clones the object using the `cloneDeep` method.
4. `console.log(obj2);` - prints out the cloned object.

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15).

onelinerhub: [How do I use Lodash to copy an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-copy-an-object-in-javascript)