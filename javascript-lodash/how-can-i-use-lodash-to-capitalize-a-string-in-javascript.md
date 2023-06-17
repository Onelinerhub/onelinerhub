# How can I use Lodash to capitalize a string in JavaScript?
// plain

To capitalize a string in JavaScript using Lodash, you can use the `_.startCase` method. This method takes a string and converts it to start with an uppercase letter.

```javascript
const _ = require('lodash');

const str = 'hello world';

const result = _.startCase(str);

console.log(result);
// Output: 'Hello World'
```

The code above consists of the following parts:

1. `const _ = require('lodash');` - This line imports the Lodash library so that the `_.startCase` method can be used.
2. `const str = 'hello world';` - This line defines a variable `str` and assigns it the value of the string `'hello world'`.
3. `const result = _.startCase(str);` - This line uses the `_.startCase` method to capitalize the string `str` and assigns the result to the variable `result`.
4. `console.log(result);` - This line logs the result of the `_.startCase` method to the console.

For more information, see the [Lodash documentation](https://lodash.com/docs/4.17.15#startCase).

onelinerhub: [How can I use Lodash to capitalize a string in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-capitalize-a-string-in-javascript)