# How can I use Lodash to split a string in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to split a string in JavaScript using the `_.split()` function.

## Example code

```
const str = 'Hello world';
const splitStr = _.split(str, ' ');

console.log(splitStr);
```

## Output example

```
[ 'Hello', 'world' ]
```

The `_.split()` function takes two arguments: the string to be split and the separator. In this example, the separator is a space character, so the string is split into two parts.

The function returns an array of strings containing the parts of the original string.

## Code explanation

- `const str = 'Hello world';` - creating a string variable
- `const splitStr = _.split(str, ' ');` - splitting the string using Lodash's `_.split()` function
- `console.log(splitStr);` - logging the result

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN - String.prototype.split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)

onelinerhub: [How can I use Lodash to split a string in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-split-a-string-in-javascript)