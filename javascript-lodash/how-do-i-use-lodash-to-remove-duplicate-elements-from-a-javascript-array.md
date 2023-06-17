# How do I use Lodash to remove duplicate elements from a JavaScript array?
// plain

Using Lodash, you can remove duplicate elements from a JavaScript array by using the `uniq` method. `uniq` takes an array and returns a duplicate-free version of the array.

For example:

```javascript
const _ = require('lodash');

const arr = [1, 1, 2, 3, 3, 4];
const result = _.uniq(arr);

console.log(result); // [1, 2, 3, 4]
```

The `uniq` method will iterate through the array and remove any duplicate values. It will return an array with only unique values.

## Code explanation


- `require('lodash')`: Imports the Lodash library.
- `_.uniq(arr)`: The `uniq` method takes an array and returns a duplicate-free version of the array.
- `console.log(result)`: Logs the result of the `uniq` method to the console.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [Lodash `uniq` Method](https://lodash.com/docs/4.17.15#uniq)

onelinerhub: [How do I use Lodash to remove duplicate elements from a JavaScript array?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-duplicate-elements-from-a-javascript-array)