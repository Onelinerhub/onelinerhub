# How do I use Lodash's isnil method in JavaScript?
// plain

The `_.isNil()` method in Lodash is used to check if a value is `null` or `undefined`. It returns `true` if the value is `null` or `undefined`, and `false` if it is any other value.

Here is an example of using `_.isNil()`:

```
const _ = require('lodash');

const value = null;

console.log(_.isNil(value));
// output: true
```

In the example above, `_.isNil()` is used to check if the value of `value` is `null` or `undefined`. The output is `true` because the value of `value` is `null`.

The parts of the code are:
- `const _ = require('lodash');`: This is used to import Lodash into the project.
- `const value = null`: This is the value that is being checked.
- `console.log(_.isNil(value))`: This is the call to the `_.isNil()` method, which is used to check if the value of `value` is `null` or `undefined`.

## Helpful links
- [Lodash Documentation - _.isNil()](https://lodash.com/docs/4.17.15#isNil)

onelinerhub: [How do I use Lodash's isnil method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-isnil-method-in-javascript)