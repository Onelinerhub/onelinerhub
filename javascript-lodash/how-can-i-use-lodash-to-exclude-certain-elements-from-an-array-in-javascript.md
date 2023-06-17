# How can I use Lodash to exclude certain elements from an array in JavaScript?
// plain

Using Lodash, you can exclude certain elements from an array using the `_.pull` method. This method takes an array and one or more values to remove from the array. Here is an example:

```
const array = [1,2,3,4,5];
_.pull(array, 3);
console.log(array);
// Output: [1,2,4,5]
```

The `_.pull` method will remove the value of `3` from the array, resulting in an array with the elements `1,2,4,5`.

The `_.pull` method is useful for removing unwanted values from an array. It is also possible to pass an array of values to the `_.pull` method, which will remove all of those values from the array.

Here is an example of passing an array to `_.pull`:

```
const array = [1,2,3,4,5];
const valuesToRemove = [3,4];
_.pull(array, valuesToRemove);
console.log(array);
// Output: [1,2,5]
```

In this example, the values `3` and `4` are passed to the `_.pull` method, which will remove those values from the array. The resulting array is `[1,2,5]`.

For more information on Lodash's `_.pull` method, please refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#pull).

onelinerhub: [How can I use Lodash to exclude certain elements from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-exclude-certain-elements-from-an-array-in-javascript)