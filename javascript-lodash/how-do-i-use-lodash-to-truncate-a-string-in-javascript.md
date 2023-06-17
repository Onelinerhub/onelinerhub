# How do I use Lodash to truncate a string in JavaScript?
// plain

Using Lodash, you can truncate a string in JavaScript by using the `_.truncate()` method. This method takes two parameters, the string to truncate and an optional options object.

The options object can take a number of properties, such as `length` (the length of the truncated string), `omission` (the string to use in place of the truncated text), and `separator` (the string to use to separate the truncated text from the omitted text).

For example, to truncate a string to a length of 10 characters, with an omission of '...' and a separator of '|', you can use the following code:

```javascript
let truncatedString = _.truncate('This is a long string', {
    length: 10,
    omission: '...',
    separator: '|'
});

console.log(truncatedString);
```

## Output example

```
This is|...
```

The code is composed of the following parts:

- `let truncatedString =` declares a variable to hold the result of the truncation.
- `_.truncate('This is a long string', {...})` is the Lodash method call, passing in the string to be truncated and the options object.
- `length: 10` sets the length of the truncated string to 10 characters.
- `omission: '...'` sets the string to use in place of the truncated text.
- `separator: '|'` sets the string to use to separate the truncated text from the omitted text.
- `console.log(truncatedString)` prints the result to the console.

## Helpful links

- [Lodash Documentation - _.truncate](https://lodash.com/docs/4.17.15#truncate)

onelinerhub: [How do I use Lodash to truncate a string in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-truncate-a-string-in-javascript)