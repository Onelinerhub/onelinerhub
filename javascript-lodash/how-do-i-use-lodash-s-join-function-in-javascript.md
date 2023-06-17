# How do I use Lodash's join function in JavaScript?
// plain

Lodash's `join` function is used to join the elements of an array into a string. It takes two arguments, the array to join and an optional separator string. It returns a string of the joined elements.

## Example


```
const _ = require('lodash');

const arr = ['a', 'b', 'c'];
const sep = '-';

const joined = _.join(arr, sep);

console.log(joined);
```

## Output example

```
a-b-c
```

The code above uses Lodash's `join` function to join the elements of an array `arr` with a separator `sep` and logs the result to the console.

## Code explanation

- `const _ = require('lodash');`: imports Lodash library
- `const arr = ['a', 'b', 'c'];`: creates an array with elements `a`, `b`, `c`
- `const sep = '-';`: creates a separator string `-`
- `const joined = _.join(arr, sep);`: calls Lodash's `join` function with arguments `arr` and `sep`
- `console.log(joined);`: logs the result of `_.join` to the console

## Helpful links
- [Lodash Documentation - join](https://lodash.com/docs/4.17.15#join)

onelinerhub: [How do I use Lodash's join function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-join-function-in-javascript)