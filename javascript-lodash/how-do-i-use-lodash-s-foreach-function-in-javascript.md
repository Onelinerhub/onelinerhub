# How do I use Lodash's forEach function in JavaScript?
// plain

Lodash's forEach function is a powerful tool for iterating over collections in JavaScript. It allows you to execute a function for each item in the array or object. This is useful for performing operations on each item such as transforming values, filtering, or performing calculations.

Here is an example of how to use Lodash's forEach function:
```
const _ = require('lodash');

const array = [1, 2, 3, 4];

_.forEach(array, (item) => {
  console.log(item * 2);
});

// Output:
// 2
// 4
// 6
// 8
```

The code above uses Lodash's forEach function to iterate over the array and log the result of multiplying each item by 2.

The forEach function takes two arguments. The first argument is the collection to iterate over. The second argument is a callback function that will be executed on each item in the collection. The callback function takes three arguments. The first argument is the value of the item, the second argument is the index of the item, and the third argument is the collection itself.

## Code explanation


* `const _ = require('lodash');` - This is how we import the Lodash library.
* `const array = [1, 2, 3, 4];` - This is the array we will iterate over.
* `_.forEach(array, (item) => {` - This is the forEach function. It takes two arguments - the collection to iterate over and a callback function.
* `console.log(item * 2);` - This is the callback function. It takes three arguments - the value of the item, the index of the item, and the collection itself. In this case, we are logging the result of multiplying each item by 2.

Here are some ## Helpful links

* [Lodash Documentation](https://lodash.com/docs/4.17.15)
* [MDN forEach Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

onelinerhub: [How do I use Lodash's forEach function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-foreach-function-in-javascript)