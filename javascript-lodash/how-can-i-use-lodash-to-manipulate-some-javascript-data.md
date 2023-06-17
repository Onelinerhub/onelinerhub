# How can I use Lodash to manipulate some JavaScript data?
// plain

Lodash is a library of JavaScript functions that help you manipulate data. Here is an example of how you can use Lodash to manipulate some JavaScript data:

```
// Import lodash library
const _ = require('lodash');

// Define some data
const data = [
  {name: 'John', age: 20},
  {name: 'Jane', age: 25},
  {name: 'Bob', age: 30},
];

// Use Lodash to find the oldest person
const oldest = _.maxBy(data, 'age');

console.log(oldest);
```

## Output example

```
{name: 'Bob', age: 30}
```

1. `require('lodash')`: Imports the Lodash library into the program.
2. `const data = [...]`: Defines an array of data.
3. `_.maxBy(data, 'age')`: Uses the Lodash `maxBy` function to find the object with the highest age value.
4. `console.log(oldest)`: Prints the oldest person to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [Lodash Tutorial](https://www.tutorialspoint.com/lodash/index.htm)

onelinerhub: [How can I use Lodash to manipulate some JavaScript data?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-manipulate-some-javascript-data)