# How do I use Lodash to flatten a JavaScript array?
// plain

[Lodash](https://lodash.com/) is a JavaScript library that provides utility functions for common programming tasks. One of these tasks is flattening a JavaScript array.

To use Lodash to flatten an array, you can use the **_.flatten()** method. This method takes an array as an argument and returns a new array with all sub-array elements concatenated into it.

For example, the following code block:

```
const array = [1, [2, [3, [4]], 5]];

const flattenedArray = _.flatten(array);

console.log(flattenedArray);
```

will output the following:

```
[1, 2, 3, 4, 5]
```

The code block above consists of three parts:

1. The first line declares a variable called **array** and assigns it to an array of nested elements.
2. The second line calls the Lodash **_.flatten()** method on the **array** variable, and assigns the result to the **flattenedArray** variable.
3. The third line uses the **console.log()** method to log the contents of the **flattenedArray** variable to the console.

For more information about Lodash and the **_.flatten()** method, please refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#flatten).

onelinerhub: [How do I use Lodash to flatten a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-flatten-a-javascript-array)