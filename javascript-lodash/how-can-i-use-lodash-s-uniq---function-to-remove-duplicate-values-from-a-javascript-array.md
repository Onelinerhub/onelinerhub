# How can I use Lodash's uniq() function to remove duplicate values from a JavaScript array?
// plain

The `uniq()` function from Lodash is a helpful tool for removing duplicate values from a JavaScript array. To use it, you first need to import the function from Lodash into your project:

```javascript
import uniq from 'lodash.uniq';
```

Then, you can call the function on the array you want to filter:

```javascript
const myArray = [1, 2, 3, 4, 1, 2];
const filteredArray = uniq(myArray);

console.log(filteredArray); // [1, 2, 3, 4]
```

The `uniq()` function will take the array as an argument and return a new array with only the unique values from the original array. In the example above, `myArray` contains two duplicate values (`1` and `2`), and `filteredArray` is an array containing only the unique values (`1`, `2`, `3`, and `4`).

It's important to note that `uniq()` uses a shallow comparison for determining uniqueness, so objects with the same values will not be filtered out. If you need to filter out objects as well, you can use `uniqBy()` instead.

## Code explanation


- `import uniq from 'lodash.uniq';` – imports the `uniq()` function from Lodash into the project.
- `const myArray = [1, 2, 3, 4, 1, 2];` – creates an array with duplicate values.
- `const filteredArray = uniq(myArray);` – calls the `uniq()` function on the array and stores the result in a new variable.
- `console.log(filteredArray);` – logs the filtered array to the console.

For more information about the `uniq()` function, check out the [Lodash documentation](https://lodash.com/docs/4.17.15#uniq).

onelinerhub: [How can I use Lodash's uniq() function to remove duplicate values from a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-uniq---function-to-remove-duplicate-values-from-a-javascript-array)