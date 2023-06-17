# How do I get the last element in an array using Lodash in JavaScript?
// plain

To get the last element in an array using Lodash in JavaScript, you can use the `_.last()` method. This method takes the array as an argument and returns the last element of the array.

```javascript
const array = ['a', 'b', 'c', 'd'];

const lastElement = _.last(array);

console.log(lastElement); // 'd'
```

The `_.last()` method is part of the [Lodash](https://lodash.com/) library, which is a JavaScript utility library that provides many useful functions for manipulating arrays, objects, and strings.

The code above consists of the following parts:

1. `const array = ['a', 'b', 'c', 'd'];` - This line declares a constant variable `array` and assigns an array of strings to it.

2. `const lastElement = _.last(array);` - This line calls the `_.last()` method with the `array` as an argument, and stores the returned value in a constant variable `lastElement`.

3. `console.log(lastElement);` - This line logs the value of `lastElement` to the console.

4. `// 'd'` - This is the output of the code, which is the last element of the array `d`.

## Helpful links
- [Lodash - _.last()](https://lodash.com/docs/4.17.15#last)

onelinerhub: [How do I get the last element in an array using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-get-the-last-element-in-an-array-using-lodash-in-javascript)