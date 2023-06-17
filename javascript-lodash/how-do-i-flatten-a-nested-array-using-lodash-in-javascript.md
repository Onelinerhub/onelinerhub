# How do I flatten a nested array using Lodash in JavaScript?
// plain

Using Lodash, you can flatten a nested array in JavaScript with the `_.flatten()` method.

## Example


```
let array = [1, [2, [3, [4]], 5]];
let flattenedArray = _.flatten(array);

console.log(flattenedArray);
```

## Output example

```
[1, 2, 3, 4, 5]
```

The `_.flatten()` method takes a nested array as an argument and returns a flattened array. In the example above, the nested array `[1, [2, [3, [4]], 5]` is flattened into a single-level array `[1, 2, 3, 4, 5]`.

The `_.flatten()` method also takes an optional argument of `depth` which specifies how deep the flattening should be. If `depth` is not specified, the array will be flattened to a single level.

The `_.flatten()` method is part of the Lodash library and can be imported into your project using `import _ from 'lodash'` or `const _ = require('lodash')`.

## Helpful links

- [Lodash Documentation for _.flatten()](https://lodash.com/docs/4.17.15#flatten)
- [MDN Documentation for import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
- [MDN Documentation for require](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/require)

onelinerhub: [How do I flatten a nested array using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-flatten-a-nested-array-using-lodash-in-javascript)