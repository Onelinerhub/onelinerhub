# How do I capitalize a string using Lodash in JavaScript?
// plain

Using Lodash in JavaScript, we can capitalize a string by using the `_.startCase()` method. This method will take a string and capitalize the first letter of each word.

## Example

```
const str = 'hello world';
const result = _.startCase(str);
console.log(result);
```
## Output example

```
Hello World
```

The `_.startCase()` method takes a string as an argument and returns a new string with the first letter of each word capitalized. It will also remove any underscores or hyphens in the string and replace them with spaces.

For example, if we have a string `'hello_world'`, the `_.startCase()` method will return `'Hello World'`.

We can also use the `_.upperCase()` method to capitalize the entire string. This method takes a string as an argument and returns a new string with all the letters in uppercase.

## Example

```
const str = 'hello world';
const result = _.upperCase(str);
console.log(result);
```
## Output example

```
HELLO WORLD
```

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [_.startCase()](https://lodash.com/docs/4.17.15#startCase)
- [_.upperCase()](https://lodash.com/docs/4.17.15#upperCase)

onelinerhub: [How do I capitalize a string using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-capitalize-a-string-using-lodash-in-javascript)