# How can I check if a variable is null or undefined using Lodash in JavaScript?
// plain

To check if a variable is null or undefined using Lodash in JavaScript, you can use the _.isNil() method. This method returns true if the given value is null or undefined.

## Example code

```
const _ = require('lodash');

let a = null;
let b = undefined;
let c = 0;

console.log(_.isNil(a)); // true
console.log(_.isNil(b)); // true
console.log(_.isNil(c)); // false
```

## Output example

```
true
true
false
```

The _.isNil() method takes in one argument, the value to be tested. In the example above, the values of `a` and `b` are null and undefined respectively. The _.isNil() method returns true for both of these values since they are both null or undefined. The value of `c` is 0, so the _.isNil() method returns false.

## Helpful links
- [Lodash Documentation - isNil](https://lodash.com/docs/4.17.15#isNil)

onelinerhub: [How can I check if a variable is null or undefined using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-check-if-a-variable-is-null-or-undefined-using-lodash-in-javascript)