# How can I use Lodash to union two JavaScript arrays?
// plain

Using Lodash's union method, two JavaScript arrays can be combined into one. This method will remove duplicate values from the two arrays and return a new array with all unique values from both.

## Example code

```
const arr1 = [1, 2, 3];
const arr2 = [2, 3, 4];

const unionArr = _.union(arr1, arr2);

console.log(unionArr);
```

## Output example

```
[1, 2, 3, 4]
```

The code above uses Lodash's union method to combine two arrays, `arr1` and `arr2`. The method returns a new array, `unionArr`, which contains all unique values from both `arr1` and `arr2`.

## Code explanation

* `_.union`: This is the Lodash method used to combine two arrays.
* `arr1` and `arr2`: These are the two arrays being combined.
* `unionArr`: This is the new array which contains all unique values from both `arr1` and `arr2`.

## Helpful links
* [Lodash Documentation](https://lodash.com/docs/)
* [Lodash Union Method](https://lodash.com/docs/4.17.15#union)

onelinerhub: [How can I use Lodash to union two JavaScript arrays?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-union-two-javascript-arrays)