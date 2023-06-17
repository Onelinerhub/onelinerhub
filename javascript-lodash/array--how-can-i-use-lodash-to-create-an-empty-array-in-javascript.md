# array

How can I use Lodash to create an empty array in JavaScript?
// plain

Using Lodash, you can create an empty array in JavaScript with the `_.fill` method. This method takes three parameters: the array to be filled, the value to fill it with, and the start and end indices. The following example code will create an empty array with a length of 5:

```
const emptyArray = _.fill(Array(5), 0);
console.log(emptyArray); // Output: [0, 0, 0, 0, 0]
```

The `_.fill` method takes three parameters:

- **array**: The array to be filled.
- **value**: The value to fill the array with.
- **start** (optional): The index at which to start filling the array. Defaults to 0.
- **end** (optional): The index at which to end filling the array. Defaults to the length of the array.

In this example, the **array** parameter is an array created with the `Array` constructor, the **value** parameter is set to `0`, and the **start** and **end** parameters are omitted, so they default to `0` and the length of the array, respectively.

For more information, check out the [Lodash documentation for `_.fill`](https://lodash.com/docs/4.17.15#fill).

onelinerhub: [array

How can I use Lodash to create an empty array in JavaScript?](https://onelinerhub.com/javascript-lodash/array--how-can-i-use-lodash-to-create-an-empty-array-in-javascript)