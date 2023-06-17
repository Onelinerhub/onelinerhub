# How can I calculate a percentage using Lodash in JavaScript?
// plain

Using Lodash in JavaScript, you can easily calculate a percentage with a few lines of code. Here's an example of how to do it:

```
// Calculate a percentage
const _ = require('lodash');

// Define the total and the part
const total = 100;
const part = 25;

// Calculate the percentage
const percentage = _.round(_.multiply(_.divide(part, total), 100), 2);

console.log(percentage);
// Output: 25
```

The code above works as follows:

1. The `const _ = require('lodash');` line imports the Lodash library.
2. The `const total = 100;` and `const part = 25;` lines define the total and part values.
3. The `const percentage = _.round(_.multiply(_.divide(part, total), 100), 2);` line divides the part by the total, multiplies the result by 100, and rounds it to two decimal places.
4. The `console.log(percentage);` line prints the resulting percentage.

For more information, you can check out the [Lodash documentation](https://lodash.com/docs/4.17.15) and the [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round).

onelinerhub: [How can I calculate a percentage using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-calculate-a-percentage-using-lodash-in-javascript)