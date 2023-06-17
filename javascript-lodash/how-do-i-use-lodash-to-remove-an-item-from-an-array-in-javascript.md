# How do I use Lodash to remove an item from an array in JavaScript?
// plain

Using Lodash to remove an item from an array in JavaScript is quite simple. You can use the _.remove() method to do this.

The _.remove() method takes two parameters - the array and the item to remove from the array. The method returns the modified array with the item removed.

## Example


```
const _ = require('lodash');

let arr = [1, 2, 3, 4, 5];

let removed = _.remove(arr, (item) => item === 3);

console.log(arr); // [1, 2, 4, 5]
console.log(removed); // [3]
```

The code above uses the _.remove() method to remove the item 3 from the array `arr`. The modified array with the item removed is then logged to the console.

The _.remove() method takes a callback function as a second parameter which is used to determine which item to remove from the array. The callback function should return `true` if the item should be removed from the array and `false` otherwise.

## Helpful links
- [Lodash _.remove() Docs](https://lodash.com/docs/#remove)

onelinerhub: [How do I use Lodash to remove an item from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-an-item-from-an-array-in-javascript)