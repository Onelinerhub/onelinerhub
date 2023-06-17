# How can I use Lodash to create a hashmap in Javascript?
// plain

A hashmap is an efficient data structure that maps keys to values. Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to create a hashmap in JavaScript.

## Example code

```
const _ = require('lodash');

const myHashMap = _.zipObject(['key1', 'key2'], ['value1', 'value2']);

console.log(myHashMap);
```

## Output example

```
{ key1: 'value1', key2: 'value2' }
```

In the example code above:
- `require('lodash')` imports the Lodash library.
- `_.zipObject` takes two arrays and creates a hashmap from them. The first array contains the keys and the second array contains the corresponding values.
- `console.log(myHashMap)` prints the hashmap to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs)
- [MDN - ZipObject](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/zipObject)

onelinerhub: [How can I use Lodash to create a hashmap in Javascript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-create-a-hashmap-in-javascript)