# How do I use the Lodash chain method in JavaScript?
// plain

The Lodash chain method is a powerful utility in JavaScript that allows you to chain multiple functions together to create a single sequence of operations. It is a great way to simplify complex logic and reduce the amount of code you need to write. Here is an example of how to use the chain method:

```
const _ = require('lodash');

const input = [1, 2, 3, 4, 5];

const output = _.chain(input)
  .map(x => x * 2)
  .filter(x => x > 5)
  .value();

console.log(output);
```

## Output example

```
[ 6, 8, 10 ]
```

The code above:
1. Imports the Lodash library with `const _ = require('lodash');`
2. Creates an array of numbers with `const input = [1, 2, 3, 4, 5];`
3. Begins the chain with `_.chain(input)`
4. Maps each element to double its value with `.map(x => x * 2)`
5. Filters the array to only keep elements greater than 5 with `.filter(x => x > 5)`
6. Ends the chain with `.value()`
7. Logs the output to the console with `console.log(output);`

For more information about the Lodash chain method, see the [Lodash documentation](https://lodash.com/docs/4.17.15#chain).

onelinerhub: [How do I use the Lodash chain method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-the-lodash-chain-method-in-javascript)