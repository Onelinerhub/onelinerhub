# How do I use Lodash to create a sample in JavaScript?
// plain

Lodash is a library of JavaScript utility functions that can be used to simplify common programming tasks. To create a sample in JavaScript using Lodash, you can use the `_.sample()` function. This function takes an array as an argument and returns a randomly selected element from the array.

## Example code

```
const fruits = ['apple', 'banana', 'kiwi', 'mango', 'orange'];

const sampleFruit = _.sample(fruits);

console.log(sampleFruit);
```

## Output example

```
mango
```

The code above creates an array of fruits, then uses the `_.sample()` function to select a random element from the array and store it in the `sampleFruit` variable. Finally, the `sampleFruit` variable is logged to the console.

The parts of this code are:
1. `const fruits = ['apple', 'banana', 'kiwi', 'mango', 'orange'];`: This creates an array of fruits.
2. `const sampleFruit = _.sample(fruits);`: This uses the `_.sample()` function to select a random element from the `fruits` array and store it in the `sampleFruit` variable.
3. `console.log(sampleFruit);`: This logs the `sampleFruit` variable to the console.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [_.sample() Documentation](https://lodash.com/docs/4.17.15#sample)

onelinerhub: [How do I use Lodash to create a sample in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-create-a-sample-in-javascript)