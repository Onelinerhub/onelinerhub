# How do I check if an array contains a value using Lodash in JavaScript?
// plain

The easiest way to check if an array contains a value using Lodash in JavaScript is to use the _.includes() method. This method takes two arguments, the array to search and the value to search for. The method returns a boolean value of true if the value is found in the array, and false if the value is not found.

## Example

```
const array = [1, 2, 3, 4];
const value = 3;
const result = _.includes(array, value);
console.log(result); // true
```

This example code uses the Lodash _.includes() method to check if the array contains the value of 3. The method returns a boolean value of true, indicating that the value was found in the array.

## Code explanation

- `const array = [1, 2, 3, 4];`: This line declares a constant variable called array and assigns it an array of values.
- `const value = 3;`: This line declares a constant variable called value and assigns it a value of 3.
- `const result = _.includes(array, value);`: This line uses the Lodash _.includes() method to check if the array contains the value of 3.
- `console.log(result);`: This line logs the result of the _.includes() method to the console.

## Helpful links
- [Lodash Documentation - _.includes()](https://lodash.com/docs/#includes)

onelinerhub: [How do I check if an array contains a value using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-check-if-an-array-contains-a-value-using-lodash-in-javascript)