# How do I use Lodash to create a dictionary in JavaScript?
// plain

Using Lodash, you can create a dictionary in JavaScript by using the `_.fromPairs()` method. This method takes an array of key-value pairs and creates an object from them.

For example:
```
const pairs = [
  ['name', 'John'],
  ['age', 25],
  ['location', 'New York']
];

const dictionary = _.fromPairs(pairs);

console.log(dictionary);
```
## Output example

```
{ name: 'John', age: 25, location: 'New York' }
```

The code above creates a dictionary from an array of key-value pairs. The `pairs` variable is an array of arrays, each containing a key and a value. The `_.fromPairs()` method takes this array and creates an object from it. The resulting object is assigned to the `dictionary` variable, which is then logged to the console.

The following list contains the parts of the code and their explanations:
- `const pairs = [ ... ]`: This declares a constant variable `pairs` and assigns it an array of arrays, each containing a key and a value.
- `const dictionary = _.fromPairs(pairs)`: This declares a constant variable `dictionary` and assigns it the result of calling the `_.fromPairs()` method with the `pairs` array as an argument. This creates an object from the array of key-value pairs.
- `console.log(dictionary)`: This logs the `dictionary` object to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [MDN _.fromPairs() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries)

onelinerhub: [How do I use Lodash to create a dictionary in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-create-a-dictionary-in-javascript)