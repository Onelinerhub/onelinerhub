# How can I use Lodash to check if a string is valid JSON in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. One of the tasks it can be used for is to check if a string is valid JSON. To do this, Lodash provides the `_.isJSON()` method.

## Example code

```
const _ = require('lodash');

const str = '{"name": "John", "age": 30}';

console.log(_.isJSON(str));
```

## Output example

```
true
```

The code above imports the Lodash library and then defines a string `str` which contains valid JSON. The `_.isJSON()` method is then used to check if the string is valid JSON and the result is logged to the console. The output is `true`, indicating that the string is valid JSON.

## Code explanation

- `require('lodash')`: imports the Lodash library
- `const str = '{"name": "John", "age": 30}'`: defines a string containing valid JSON
- `_.isJSON(str)`: checks if the string is valid JSON
- `console.log(_.isJSON(str))`: logs the result of the `_.isJSON()` method to the console

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [_.isJSON() Documentation](https://lodash.com/docs/4.17.15#isJSON)

onelinerhub: [How can I use Lodash to check if a string is valid JSON in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-check-if-a-string-is-valid-json-in-javascript)