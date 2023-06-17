# How can I determine the size of a JavaScript object using Lodash?
// plain

Using Lodash, you can determine the size of a JavaScript object with the `size` method. This method returns the number of own enumerable string keyed properties of an object.

## Example

```
const _ = require('lodash');

const obj = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30
};

const size = _.size(obj);
console.log(size);
```
## Output example

```
3
```

## Code explanation

- `const _ = require('lodash');`: This line imports the Lodash library.
- `const obj = {...}`: This line creates an object with three key-value pairs.
- `const size = _.size(obj);`: This line uses the `size` method to determine the size of the object.
- `console.log(size);`: This line logs the size of the object to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)

onelinerhub: [How can I determine the size of a JavaScript object using Lodash?](https://onelinerhub.com/javascript-lodash/how-can-i-determine-the-size-of-a-javascript-object-using-lodash)