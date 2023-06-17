# How do I use Lodash to return distinct values in a JavaScript array?
// plain

Lodash is a JavaScript utility library that provides a lot of useful functions to work with JavaScript objects and arrays. One of the useful functions it provides is the `_.uniq()` function which can be used to get distinct values from an array.

```
const fruits = ["Apple", "Banana", "Mango", "Apple", "Orange", "Banana"];

const distinctFruits = _.uniq(fruits);

console.log(distinctFruits);
```

The output of the above code will be:

```
[ 'Apple', 'Banana', 'Mango', 'Orange' ]
```

The `_.uniq()` function takes an array as an argument and returns an array of distinct values from the given array. It uses strict equality (`===`) to compare values.

The code can be broken down into the following parts:

1. **Declare an array of fruits** - The first line of code declares an array of fruits containing some duplicate values.

2. **Call the `_.uniq()` function** - The `_.uniq()` function is called with the array of fruits as an argument.

3. **Log the result** - The result of the `_.uniq()` function is logged to the console.

Here are some relevant links for further reading:

- [Lodash Documentation](https://lodash.com/docs/)
- [_.uniq() Documentation](https://lodash.com/docs/4.17.15#uniq)

onelinerhub: [How do I use Lodash to return distinct values in a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-return-distinct-values-in-a-javascript-array)