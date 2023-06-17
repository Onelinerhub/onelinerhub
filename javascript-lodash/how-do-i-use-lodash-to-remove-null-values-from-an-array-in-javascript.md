# How do I use Lodash to remove null values from an array in JavaScript?
// plain

Using Lodash to remove null values from an array in JavaScript is quite simple. Here is an example code block to demonstrate:

```
//Example array with null values
let array = [1, null, 2, 3, null, 4, 5];

//Using Lodash to remove null values
let filteredArray = _.without(array, null);

//Output
console.log(filteredArray); // [1, 2, 3, 4, 5]
```

The code above uses the Lodash `without` method to filter out any values that are `null` from the `array` variable. The output of the code will be a new array without any null values.

## Code explanation


- `let array = [1, null, 2, 3, null, 4, 5]`: This is the array we will be filtering.
- `let filteredArray = _.without(array, null)`: This is the Lodash `without` method, which takes two arguments. The first argument is the array we want to filter, and the second argument is the value we want to remove. In this case, we want to remove any values that are `null`.
- `console.log(filteredArray)`: This will output the filtered array to the console.

Here are some relevant links for more information:

- [Lodash Documentation - Without](https://lodash.com/docs/4.17.15#without)
- [MDN - Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

onelinerhub: [How do I use Lodash to remove null values from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-null-values-from-an-array-in-javascript)